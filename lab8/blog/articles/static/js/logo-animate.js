$(document).ready(function() {
    // Анимация логотипа при наведении
    $('.header img').hover(
        function() {
            // Увеличиваем логотип
            $(this).animate({
                width: '338px'  // было 318px
            }, 300);
        },
        function() {
            // Возвращаем исходный размер
            $(this).animate({
                width: '318px'
            }, 300);
        }
    );
});