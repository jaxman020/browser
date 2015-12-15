from django.conf.urls import url
from opera import views


urlpatterns = [
            url(r'^$', views.opera, name='opera'),
]