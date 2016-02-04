from django.conf.urls import url

from newsletter import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^base/$', views.base, name='base'),
    url(r'^about/$', views.about, name='about'),
]
