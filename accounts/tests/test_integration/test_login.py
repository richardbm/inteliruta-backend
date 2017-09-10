from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
from  accounts.tests.utils import utils
from unittest.mock import patch
from model_mommy import mommy


class TestLoginAdmin(APITestCase):

    def setUp(self):
        self.c = APIClient()
        User.objects.create_superuser(**utils.create_superuser())

    @patch('accounts.views.requests')
    def test_signup_facebook_mobile(self, requests):
        """
        Permite a los usuarios Loguearse con facebook, si no estan registrados
        debe indicar en su respuesta que el usuario aún no ha aceptado los
        terminos y condiciones
        :return: 
        """
        data = {
            'access_token': "123456",
            'redirectUri': "http://localhost"
        }

        data_response = '{'\
            '"id": "123",'\
            '"first_name": "jhon",'\
            '"last_name": "doe",'\
            '"hometown": {' \
                    '"id": 123456,' \
                    '"name":"Zulia, Venezuela"' \
            '},'\
            '"email": "doe@mail.com",'\
            '"picture":{'\
                '"data": {'\
                    '"url": "face.com"'\
                '}'\
            '}'\
        '}'

        url = 'https://graph.facebook.com/v2.8/me?' \
                  'fields=id,last_name,first_name,email,hometown,picture.type(normal)'
        requests.get.return_value.text = data_response
        requests.get.return_value.status_code= 200


        response = self.c.post('/mobile/accounts/signup-facebook/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertIn('token', response.data.keys())

    @patch('accounts.views.requests')
    def test_signup_facebook_mobile_inactive(self, requests):
        """
        Permite a los usuarios Loguearse con facebook, si no estan registrados
        debe indicar en su respuesta que el usuario aún no ha aceptado los
        terminos y condiciones
        :return: 
        """

        user = mommy.make("accounts.user", is_active=False, facebook_id="123")

        data = {
            'access_token': "123456",
            'redirectUri': "http://localhost"
        }

        data_response = '{'\
            '"id": "123",'\
            '"first_name": "jhon",'\
            '"last_name": "doe",'\
            '"hometown": {' \
                    '"id": 123456,' \
                    '"name":"Zulia, Venezuela"' \
            '},'\
            '"email": "doe@mail.com",'\
            '"picture":{'\
                '"data": {'\
                    '"url": "face.com"'\
                '}'\
            '}'\
        '}'

        url = 'https://graph.facebook.com/v2.8/me?' \
                  'fields=id,last_name,first_name,email,hometown,picture.type(normal)'
        requests.get.return_value.text = data_response
        requests.get.return_value.status_code = 200


        response = self.c.post('/mobile/accounts/signup-facebook/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.content)