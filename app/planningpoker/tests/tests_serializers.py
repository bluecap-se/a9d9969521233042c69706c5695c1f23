from django.test import TestCase

from .. import models
from .. import serializers

"""
Both serializers are ModelSerializers without any additional functionality
on top of Django Model. The tests are therefore slim.
"""


class SerializerTestCase(TestCase):

    def setUp(self):
        self.poll = models.Poll(name='abc', username='Olle')
        self.poll.save()

    def test_poll_should_pass(self):
        input = {
            'name': 'abc',
            'username': 'Olle',
        }

        serializer_instance = serializers.PollSerializer(data=input)
        self.assertTrue(serializer_instance.is_valid(raise_exception=True))
        self.assertEqual(serializer_instance.errors, {})

    def test_poll_should_fail(self):
        serializer_instance = serializers.PollSerializer(data={})
        self.assertFalse(serializer_instance.is_valid())
        self.assertTrue('name' in serializer_instance.errors)
        self.assertTrue('username' in serializer_instance.errors)

    def test_vote_should_pass(self):
        input = {
            'username': 'Olle',
            'poll': self.poll.id,
        }

        serializer_instance = serializers.VoteSerializer(data=input)
        self.assertTrue(serializer_instance.is_valid(raise_exception=True))
        self.assertEqual(serializer_instance.errors, {})
        self.assertEqual(serializer_instance.data['vote'], None)

    def test_vote_should_fail(self):
        serializer_instance = serializers.VoteSerializer(data={})
        self.assertFalse(serializer_instance.is_valid())
        self.assertTrue('username' in serializer_instance.errors)
        self.assertTrue('poll' in serializer_instance.errors)
