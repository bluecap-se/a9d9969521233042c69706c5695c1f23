from django.conf.urls import url

from . import views


app_name = 'minime'

urlpatterns = [
    url(r'^$', views.index, name='home'),
]
