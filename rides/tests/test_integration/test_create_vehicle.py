from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from model_mommy import mommy


class TestOffer(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_create_vehicle(self):
        user = mommy.make("accounts.user")

        self.c.force_authenticate(user)

        data = {
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2002,
            "color": "rojo",
            "license_plate": "AD34TD",
            "seats": 4
        }

        response = self.c.post("/my-vehicles/", data)
        self.assertEqual(response.status_code, 201)

    def test_read_vehicle(self):
        user = mommy.make("accounts.user")
        vehicle = mommy.make("rides.vehicle", owner=user, _fill_optional=True)

        self.c.force_authenticate(user)

        data = {
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "color": vehicle.color,
            "license_plate": vehicle.license_plate,
            "seats": vehicle.seats
        }

        response = self.c.get("/my-vehicles/{}/".format(vehicle.id))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, response.data)

    def test_delete_vehicle(self):
        user = mommy.make("accounts.user")
        vehicle = mommy.make("rides.vehicle", owner=user, _fill_optional=True)

        self.c.force_authenticate(user)

        response = self.c.delete("/my-vehicles/{}/".format(vehicle.id))
        self.assertEqual(response.status_code, 204, response.data)