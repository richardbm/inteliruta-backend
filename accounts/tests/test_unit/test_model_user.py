from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password

class TestUser(APITestCase):


    def test_create_user(self):
        """
        Se debe poder registrar un usuario con facebook, solo requiere el
        facebook_id
        """

        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@email.com",
            "facebook_id": "1231231234342342423"
        }

        user = User.objects.create(**user_data)

