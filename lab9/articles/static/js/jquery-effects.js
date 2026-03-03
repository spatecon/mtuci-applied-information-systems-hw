$(document).ready(function() {
    // Подсветка поста при наведении
    $(".one-post").hover(
        function() {
            $(this).css("background-color", "rgba(255, 255, 255, 0.15)");
        },
        function() {
            $(this).css("background-color", "");
        }
    );

    // Эффект для картинки-логотипа
    $("#logo").click(function() {
        $(this).fadeOut(300).fadeIn(300);
    });
});
