from django.shortcuts import render


def create_poll(request):
    return render(request, 'create-poll.html')
