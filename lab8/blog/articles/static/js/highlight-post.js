$(document).ready(function() {
    $('.one-post').hover(
        function() {
            $(this).css('background-color', 'rgba(0,0,0,0.7)');
        },
        function() {
            $(this).css('background-color', 'rgba(0,0,0,0.1)');
        }
    );
});