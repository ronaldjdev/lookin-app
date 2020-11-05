$('.navbar-default').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.navbar-default').addClass('affix');
        console.log("OK");
    } else {
        $('.navbar-default').removeClass('affix');
    }
});

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.nav-link').addClass('affix-nav-link');
        console.log("OK");
    } else {
        $('.nav-link').removeClass('affix-nav-link');
    }
});

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.justifyButton').addClass('justifyButton-2');
        console.log("OK");
    } else {
        $('.justifyButton').removeClass('justifyButton-2');
    }
});

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('#changeLogo').attr('src','static/img/LookingHome.png');
        console.log("OK");
    } else {
        $('#changeLogo').attr('src','static/img/Looking-3-white.png');
    }
});