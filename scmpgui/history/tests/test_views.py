from django.test import TestCase, Client
from django.urls import reverse
from history.models import HistoricalRecords
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('history_main')

    def test_project_list_GET(self):
        response = self.client.get(reverse('history_main'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'history/main.html')