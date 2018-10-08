from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, reverse
from rest_framework import generics

from . import forms
from . import models
from . import serializers


VOTE_OPTIONS = (0, .5, 1, 2, 3, 5, 8, 13)


def create_poll(request):
    return render(request, 'create-poll.html', {'form': forms.PollForm})


@require_http_methods(['POST'])
def create_poll_do(request):
    # TODO: Turn function into DRF view
    poll_name = request.POST.get('name', None)
    user_name = request.POST.get('username', None)

    # TODO: Perhaps show a nicer error message to the user
    if not poll_name or not user_name:
        return HttpResponseBadRequest('This page requires all params.')

    poll = models.Poll(name=poll_name, username=user_name)
    poll.save()

    url = request.build_absolute_uri(reverse('planningpoker:view-poll', args=(poll.id,)))

    return render(request, 'poll-created.html', {'url': url, 'poll': poll})


def view_poll(request, id):
    poll = get_object_or_404(models.Poll, pk=id)
    args = {
        'poll': poll,
        'vote_options': VOTE_OPTIONS,
        'form': forms.PollForm,
    }

    return render(request, 'view-poll.html', args)


class CastVote(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer


class ViewParticipantsList(generics.ListAPIView):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer
    lookup_field = 'poll__id'

    def get_queryset(self):
        """Overrides super"""
        poll = self.request.query_params.get('poll', None)
        if not poll:
            return []

        args = dict()
        args[self.lookup_field] = poll

        return self.queryset.filter(**args)
