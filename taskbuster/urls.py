from django.conf.urls import url
from taskbuster.views import home


urlpatterns = [
    url(r'^$', home, name='index'),
    ]