from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy
from collections import OrderedDict


class TestResponseOffer(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_response_offer(self):
        user = mommy.make("accounts.user")
        offer = mommy.make("rides.offer", owner=user,
                             _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "text": "Puedes llevarme?"
        }

        response = self.c.post("/offers/{}/request/".format(offer.id), data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertDictEqual.__self__.maxDiff = None

