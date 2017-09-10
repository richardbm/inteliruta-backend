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
                           status="Di",
                             _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "text": "Puedes llevarme?"
        }

        response = self.c.post("/offers/{}/request/".format(offer.id), data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertDictEqual.__self__.maxDiff = None

    def test_accept_response_offer(self):
        user = mommy.make("accounts.user")
        offer = mommy.make("rides.offer", owner=user,
                           status="Di",
                             _fill_optional=True)
        request_post = mommy.make("rides.requestpost", offer=offer,
                                  _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "request_id": request_post.id
        }

        response = self.c.post("/my-offers/{}/accept-request/".format(offer.id), data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertDictEqual.__self__.maxDiff = None

