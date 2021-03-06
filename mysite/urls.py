"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

import home.views
from mysite import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^$', home.views.homepage, name='base_home'),
    url(r'^about/$', home.views.about, name='about'),
    url(r'^contact/$', home.views.contact, name='contact'),
    url(r'^taskbuster/', include('taskbuster.urls', namespace="taskbuster")),
    url(r'^newsletter/', include('newsletter.urls', namespace="newsletter")),
    url(r'^newsletter/accounts/', include('registration.backends.default.urls')),
    url(r'^posts/', include('posts.urls', namespace="posts")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)