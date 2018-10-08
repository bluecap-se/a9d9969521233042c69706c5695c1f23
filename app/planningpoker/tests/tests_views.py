from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rest_framework import status

from .. import models


class ViewCreatePollTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_page(self):
        response = self.client.get(reverse('planningpoker:create-poll'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ViewCreatePollDoTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_must_be_post(self):
        response = self.client.get(reverse('planningpoker:save-poll'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_no_params(self):
        response = self.client.post(reverse('planningpoker:save-poll'), data=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_should_pass(self):
        poll_name = 'Refactor'

        response = self.client.post(reverse('planningpoker:save-poll'), data={'name': poll_name, 'username': 'Olle'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(models.Poll.objects.count(), 1)
        self.assertEqual(models.Poll.objects.all()[0].name, poll_name)


class ViewViewPollTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_wrong_id(self):
        response = self.client.get(reverse('planningpoker:view-poll', kwargs=dict(id=1)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_should_pass(self):
        obj = models.Poll(name='abc', username='Olle')
        obj.save()

        response = self.client.get(reverse('planningpoker:view-poll', kwargs=dict(id=obj.id)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
