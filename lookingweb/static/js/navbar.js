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
        $('.navbar-toggler span').addClass('affix-navbar-toggler span');
        console.log("OK");
    } else {
        $('.navbar-toggler span').removeClass('affix-navbar-toggler span');
    }
});