from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from messages_.forms import SignUpForm, MessageForm


class ViewsTestCase(TestCase):
    fixtures = ['forms_testdata.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_index(self):
        resp = self.client.get(reverse('index', ))
        self.assertEqual(resp.status_code, 200)

    def test_view_favorites(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('view_favorites'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('<td>9234116074</td>' in resp.content.decode())


class FormsTestCase(TestCase):
    fixtures = ['forms_testdata.json']

    def test_sign_up_form(self):
        form_data = {'phone': '9234116076',
                     'password': 'qwerty'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_message_form(self):
        form_data = {'receiver': '9234116075',
                     'text': 'abc'}
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())
