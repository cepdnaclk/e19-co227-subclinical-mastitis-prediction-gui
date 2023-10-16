from django.test import SimpleTestCase
from django.urls import reverse, resolve
from multiple.views import dataset_upload, index, display_dataset

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('multiple_dataset_upload')
        self.assertEquals(resolve(url).func, dataset_upload)

    def test_list_url_is_resolved_2(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_list_url_is_resolved_3(self):
        url = reverse('multiple_display_dataset')
        self.assertEquals(resolve(url).func, display_dataset)