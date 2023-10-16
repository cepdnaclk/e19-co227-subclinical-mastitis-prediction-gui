from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import register_page, login_page, logout_user

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('members_register')
        self.assertEquals(resolve(url).func, register_page)

    def test_list_url_is_resolved_2(self):
        url = reverse('members_login')
        self.assertEquals(resolve(url).func, login_page)

    def test_list_url_is_resolved_3(self):
        url = reverse('members_logout')
        self.assertEquals(resolve(url).func, logout_user)

    

    