
from django.utils.crypto import get_random_string
from rest_framework.test import APITestCase, APIRequestFactory
from accounts.models import User
from rest_framework.test import force_authenticate
from django.utils.crypto import get_random_string


def create_request():
    #crear el request
    factory = APIRequestFactory()
    request = factory.get('/', {})
    return request

def create_request_post(data):
    #crear el request
    factory = APIRequestFactory()
    request = factory.post('/', data)
    return request

def create_request_url():
    #crear el request
    factory = APIRequestFactory()
    request = factory.get('/', {})
    return request

def create_request_post_url(url, data):
    #crear el request
    factory = APIRequestFactory()
    request = factory.post(url, data)
    return request

username = "Master2"
first_name = "John"
last_name = "Doe"
password = "zonia123*"
email = "zonia@mail.com"


def create_superuser():

    data_superuser = {
        'username': username,
        'password': password,
        'email': email
    }
    return data_superuser

def create_user():

    data_superuser = {
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'email': email,
        'is_staff': False,
        'hometown': "Zulia, Venezuela",
        'username': get_random_string(length=6, allowed_chars="123456789")
    }
    return data_superuser

data_login = {
    'username': username,
    'password': password
}