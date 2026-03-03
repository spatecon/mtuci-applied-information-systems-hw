var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i<foldBtns.length; i++){
    foldBtns[i].addEventListener("click", function(event) {
        var btn = event.target;
        var post = btn.closest(".one-post");
        var info = post.querySelector(".article-info");
        var text = post.querySelector(".article-text");

        if (info.style.display === "none") {
            info.style.display = "";
            text.style.display = "";
            btn.textContent = "свернуть";
        } else {
            info.style.display = "none";
            text.style.display = "none";
            btn.textContent = "развернуть";
        }
    });
}
