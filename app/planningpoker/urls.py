from django.conf.urls import url

from . import views


app_name = 'planningpoker'

urlpatterns = [
    url(r'^$', views.create_poll, name='create-poll'),
]
