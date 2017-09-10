from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy


class TestOffer(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def tttest_create_offer(self):
        user = mommy.make("accounts.user")

        self.c.force_authenticate(user)

        data = {

        }