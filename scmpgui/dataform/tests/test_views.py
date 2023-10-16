from django.test import TestCase, Client
from django.urls import reverse
from dataform.models import Record
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('dataform')

    def test_project_list_GET(self):
        response = self.client.get(reverse('dataform'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dataform/auto.html')