$(document).ready(function() {
    $(window).scroll(function() {
        var scrollTop = $(window).scrollTop();
        $(".parallax-bg").css("background-position-y", -(scrollTop * 0.5) + "px");
    });
});
