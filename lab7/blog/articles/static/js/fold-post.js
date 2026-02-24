// Находим все кнопки
var foldBtns = document.getElementsByClassName("fold-button");

// Добавляем обработчик для каждой кнопки
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        // Находим родительский элемент one-post (поднимаемся на 3 уровня вверх)
        var post = event.target.closest('.one-post');
        
        // Находим элементы, которые нужно скрыть/показать
        var articleInfo = post.querySelector('.article-info');
        var articleText = post.querySelector('.article-text');
        
        // Проверяем состояние кнопки
        if (event.target.innerHTML == "Свернуть") {
            // Скрываем элементы
            articleInfo.style.display = "none";
            articleText.style.display = "none";
            event.target.innerHTML = "Развернуть";
        } else {
            // Показываем элементы
            articleInfo.style.display = "block";
            articleText.style.display = "block";
            event.target.innerHTML = "Свернуть";
        }
    });
}