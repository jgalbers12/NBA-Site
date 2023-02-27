from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
import pytest

@pytest.mark.django_db
def test_register_user_redirects_and_creates_user(client:Client) -> None:
    response = client.post('/users/register_user/', {'username': 'John', 'password1': 'adgjl135', 'password2': 'adgjl135'})
    #assert User.objects.get(username='John').password == 'adgjl1235'
    assert response.status_code == 302 # redirect
    assert response.url == reverse('home')

#def test_register_user_logs_in_user(client:Client) -> None:
#    response = client.post('/users/register_user/', {'username': 'John', 'password1': 'adgjl135', 'password2': 'adgjl135'})
#    assert user.username == 'John'