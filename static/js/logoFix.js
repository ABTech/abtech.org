//change logo for mobile
$(document).ready(function() {
function checkWidth() {
    var windowSize = $(window).width();

    if (windowSize <= 767) {
        $('#logoImage').attr('src','static/img/ab tech.png');
    }
    else {
        $('#logoImage').attr('src','static/img/abTech_logo.png');
    }
}
// Execute on load
checkWidth();
// Bind event listener
$(window).resize(checkWidth);
})