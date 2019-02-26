$(document).ready(function () {
    $(window).keydown(function (event) {
        if (event.keyCode === 13) {
            console.log(event.keyCode);
            event.preventDefault();
            return false;
        }
    });
});