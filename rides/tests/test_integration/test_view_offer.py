from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy
from collections import OrderedDict


class TestOffer(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_view_offer(self):
        user = mommy.make("accounts.user")
        ride = mommy.make("rides.offer", owner=user,
                             _fill_optional=True)

        self.c.force_authenticate(user)

        response = self.c.get("/offers/")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual.__self__.maxDiff = None

