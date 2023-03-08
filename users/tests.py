from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
# Create your tests here.

class UserRegistration(TestCase):

    def test_user_can_register(self):
        username = 'newuser'
        response = self.client.post('/users/register_user/', data={'username': username, 
                                                            'password1': 'adgjl1357',
                                                            'password2': 'adgjl1357'})
        user = User.objects.first()
        self.assertEqual(user.username, username)

    def test_redirect_after_register(self):
        username = 'newuser'
        response = self.client.post('/users/register_user/', data={'username': username, 
                                                            'password1': 'adgjl1357',
                                                            'password2': 'adgjl1357'})
        self.assertEqual(response.url, reverse('home'))


class UserLogin(TestCase):

    def test_user_can_login_and_redirect(self):
        # weird way to do this, but whatever
        un = 'newuser'
        pw = 'adgj1357'
        new_user = User(username=un)
        new_user.set_password(pw)
        new_user.save()
        response = self.client.post('/users/login/', data={'username': un, 'password': pw})
        self.assertEqual(response.url, reverse('home'))
        self.assertTrue(self.client.login(username=un, password=pw))
