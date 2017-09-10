from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy
from collections import OrderedDict


class TestDemand(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_create_demand(self):
        user = mommy.make("accounts.user")

        self.c.force_authenticate(user)

        data = {
            "departure_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "departure_date": "2017-09-09T14:30:00-04:00",
            "arrival_date": "2017-09-09T15:30:00-04:00",
            "arrival_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "seats": 24,
            "condition": "PS",
        }


        response = self.c.post("/my-demands/", data, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        data_response = {
            "id": response.data.get("id"),
            "departure_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "departure_date": "2017-09-09T18:30:00+0000",
            "arrival_date": "2017-09-09T19:30:00+0000",
            "arrival_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "seats": 24,
            "condition": "PS",
        }

        #self.assertDictEqual.__self__.maxDiff = None
        #self.assertDictEqual(data_response, response.data, msg=response.data)


    def test_update_demand(self):
        user = mommy.make("accounts.user")
        demand = mommy.make("rides.demand", owner=user,
                             _fill_optional=True)
        offer = mommy.make("rides.offer", owner=user,
                             _fill_optional=True)
        vehicle = mommy.make("rides.vehicle", owner=user,
                             _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "accepted_offer_id":offer.id,
            "departure_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "departure_date": "2017-09-09T14:30:00-04:00",
            "arrival_date": "2017-09-09T15:30:00-04:00",
            "arrival_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "seats": 24,
            "condition": "PS",
            "condition_display": "Por puesto",
            "status_display": "Disponible",
        }


        response = self.c.put("/my-demands/{}/".format(demand.id), data, format="json")
        self.assertEqual(response.status_code, 200, response.data)
        data_response = {
            "id": response.data.get("id"),
            "departure_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "departure_date": "2017-09-09T18:30:00+0000",
            "arrival_date": "2017-09-09T19:30:00+0000",
            "arrival_address": OrderedDict({
                "latitude": "192.168.32.12",
                "longitude": "168.158.23.21",
                "text": "calle 5 de julio con av delicias",
            }),
            "seats": 24,
            "condition": "PS",
            "condition_display": "Por puesto",
            "status_display": "Disponible",
        }

        #self.assertDictEqual.__self__.maxDiff = None
        #self.assertDictEqual(data_response, response.data)