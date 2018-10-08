from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .. import models


class ViewCreatePollTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_page(self):
        response = self.client.get(reverse('planningpoker:create-poll'))
        self.assertEqual(response.status_code, 200)


class ViewCreatePollDoTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_must_be_post(self):
        response = self.client.get(reverse('planningpoker:save-poll'))
        self.assertEqual(response.status_code, 405)

    def test_view_no_params(self):
        response = self.client.post(reverse('planningpoker:save-poll'), data=None)
        self.assertEqual(response.status_code, 400)

    def test_view_should_pass(self):
        poll_name = 'Refactor'

        response = self.client.post(reverse('planningpoker:save-poll'), data={'name': poll_name, 'username': 'Olle'})
        self.assertEqual(response.status_code, 200)

        self.assertEqual(models.Poll.objects.count(), 1)
        self.assertEqual(models.Poll.objects.all()[0].name, poll_name)
