from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from . import forms
from . import models


def create_poll(request):
    return render(request, 'create-poll.html', {'form': forms.CreatePollForm})


@require_http_methods(['POST'])
def create_poll_do(request):
    poll_name = request.POST.get('name', None)
    user_name = request.POST.get('username', None)

    # TODO: Perhaps show a nicer error message to the user
    if not poll_name or not user_name:
        return HttpResponseBadRequest('This page requires all params.')

    poll = models.Poll(name=poll_name, username=user_name)
    poll.save()

    return render(request, 'poll-created.html', {'poll': poll})
