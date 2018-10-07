from django.shortcuts import render

from . import forms


def create_poll(request):
    return render(request, 'create-poll.html', {'form': forms.CreatePollForm})


def create_poll_do(request):
    pass
