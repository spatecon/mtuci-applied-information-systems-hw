from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if username and email and password:
            try:
                User.objects.get(username=username)
                return render(request, 'registration.html', {'errors': "Пользователь с таким именем уже существует"})
            except User.DoesNotExist:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return redirect('archive')
        else:
            return render(request, 'registration.html', {'errors': "Не все поля заполнены"})
    return render(request, 'registration.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                return render(request, 'login.html', {'errors': "Нет аккаунта с таким сочетанием никнейма и пароля"})
        else:
            return render(request, 'login.html', {'errors': "Не все поля заполнены"})
    return render(request, 'login.html', {})
