from django.conf.urls import url
from sarafi import views


urlpatterns = [
            url(r'^$',  views.sarafi, name='sarafi'),
]