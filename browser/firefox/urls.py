from django.conf.urls import url
from firefox import views


urlpatterns = [
               url(r'^$', views.firefox, name='firefox'),
]