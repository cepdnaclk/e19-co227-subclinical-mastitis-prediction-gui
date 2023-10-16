from django.test import SimpleTestCase
from django.urls import reverse, resolve
from history.views import ViewHistory

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('history_main')
        self.assertEquals(resolve(url).func, ViewHistory)