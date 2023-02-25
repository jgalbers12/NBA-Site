from django.test import Client
import pytest

#@pytest.mark.django_db
def test_register_user(client:Client) -> None:
    response = client.post('/users/register_user/', {'username': 'John', 'password1': 'adgjl135', 'password2': 'adgjl135'})
    assert response.status_code == 302 # redirect