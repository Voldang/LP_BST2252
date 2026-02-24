# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    # Проверка авторизации
    if request.user.is_anonymous():
        raise Http404
    
    if request.method == "POST":
        title = request.POST.get("title", "")
        text = request.POST.get("text", "")
        
        if title and text:
            # Создание новой статьи
            article = Article.objects.create(
                text=text,
                title=title,
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            # Ошибка - не все поля заполнены
            return render(request, 'create_post.html', {
                'errors': u"Не все поля заполнены",
                'title': title,
                'text': text
            })
    else:
        # GET-запрос - показываем пустую форму
        return render(request, 'create_post.html', {})