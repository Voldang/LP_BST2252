# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.models import User
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
    if request.user.is_anonymous():
        raise Http404
    
    if request.method == "POST":
        title = request.POST.get("title", "")
        text = request.POST.get("text", "")
        
        if title and text:
            article = Article.objects.create(
                text=text,
                title=title,
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            return render(request, 'create_post.html', {
                'errors': u"Не все поля заполнены",
                'title': title,
                'text': text
            })
    else:
        return render(request, 'create_post.html', {})

def login(request):
    if request.user.is_authenticated():
        return redirect('archive')
    
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {
                'error': u"Неверное имя пользователя или пароль",
                'username': username
            })
    else:
        # GET-запрос - показываем форму
        return render(request, 'login.html', {})

def register(request):
    if request.user.is_authenticated():
        return redirect('archive')
    
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        
        if username and email and password:
            try:
                User.objects.get(username=username)
                return render(request, 'register.html', {
                    'error': u"Пользователь с таким именем уже существует",
                    'username': username,
                    'email': email
                })
            except User.DoesNotExist:
                user = User.objects.create_user(username, email, password)
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect('archive')
        else:
            return render(request, 'register.html', {
                'error': u"Заполните все поля",
                'username': username,
                'email': email
            })
    else:
        # GET-запрос - показываем форму
        return render(request, 'register.html', {})

def logout(request):
    auth.logout(request)
    return redirect('archive')