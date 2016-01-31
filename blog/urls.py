from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.blog_home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
]