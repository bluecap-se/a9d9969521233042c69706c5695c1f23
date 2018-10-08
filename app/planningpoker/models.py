from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    username = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    vote = models.FloatField(null=True)
