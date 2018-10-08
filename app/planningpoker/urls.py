from django.conf.urls import url

from . import views


app_name = 'planningpoker'

urlpatterns = [
    url(r'^$', views.create_poll, name='create-poll'),
    url(r'^save-poll/?$', views.create_poll_do, name='save-poll'),
    url(r'^view-poll/(?P<id>[0-9]+)/?$', views.view_poll, name='view-poll'),
    url(r'^cast-vote/?$', views.CastVote.as_view(), name='cast-vote'),
    url(r'^cast-vote/(?P<pk>[0-9]+)/?$', views.CastVote.as_view(), name='cast-vote-edit'),
    url(r'^view-participants/?$', views.ViewParticipantsList.as_view(), name='view-participants'),
]
