from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dataform.views import DataFormView

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('dataform')
        self.assertEquals(resolve(url).func, DataFormView)