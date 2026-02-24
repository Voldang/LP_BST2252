from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'articles.views.archive', name='archive'),
    url(r'^article/new/$', 'articles.views.create_post', name='create_post'),
    url(r'^article/(?P<article_id>\d+)$', 'articles.views.get_article', name='get_article'),
    url(r'^login/$', 'articles.views.login', name='login'),
    url(r'^register/$', 'articles.views.register', name='register'),
    url(r'^logout/$', 'articles.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)