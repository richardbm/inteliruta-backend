from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy


class TestOffer(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_create_offer(self):
        user = mommy.make("accounts.user")
        vehicle = mommy.make("rides.vehicle", _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "departure_address": {
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            },
            "departure_date": "2017-09-09T14:30:00:0000",
            "arrival_date": "2017-09-09T15:30:00:0000",
            "arrival_address": {
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            },
            "vehicle_id": 1,
            "seats": 24,
            "condition": "PS",
            "price": 1234
        }

        response = self.c.post("/my-offers/", data, format="json")
        self.assertEqual(response.status_code, 201)