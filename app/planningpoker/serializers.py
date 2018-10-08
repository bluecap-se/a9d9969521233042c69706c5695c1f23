from rest_framework import serializers

from . import models


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Poll
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vote
        fields = '__all__'
