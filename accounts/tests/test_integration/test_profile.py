from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
from  accounts.tests.utils import utils
class TestLoginAdmin(APITestCase):

    def setUp(self):
        self.c = APIClient()
        self.data_user = utils.create_user()
        self.user = User.objects.create_user(**self.data_user)



    def test_view_profile(self):

        """
        se debe ver el perfil de usuario
        """

        self.c.force_authenticate(self.user)
        response = self.c.get('/accounts/profile/')
        data = self.data_user
        data['id'] = self.user.id
        data['facebook_picture_url'] = None
        data.pop('password')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, data)

