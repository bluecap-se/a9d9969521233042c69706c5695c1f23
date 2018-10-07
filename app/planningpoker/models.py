from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256)
    username = models.URLField(max_length=256)
    created = models.DateTimeField(auto_now=True)
