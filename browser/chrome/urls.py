from django.conf.urls import url
from chrome import views


urlpatterns = [
            url(r'^$',  views.chrome, name='chrome'),
]