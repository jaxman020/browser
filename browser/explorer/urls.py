from django.conf.urls import url
from explorer import views


urlpatterns = [
            url(r'^$',  views.explorer, name='explorer'),
]