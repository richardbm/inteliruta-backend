
**demand:**

**List demands:**

GET /demands/

**Response:**

```
[
    {
        "id": 4,
        "departure_date": "2017-09-09T18:30:00+0000",
        "arrival_date": "2017-09-09T19:30:00+0000",
        "departure_address": {
            "latitude": "192.168.32.12",
            "longitude": "168.169.23.21",
            "text": "calle 5 de julio con av delicias"
        },
        "arrival_address": {
            "latitude": "192.168.30.13",
            "longitude": "168.158.23.21",
            "text": "calle 5 de julio con av delicias"
        },
        "condition_display": "Por puesto",
        "vehicle": {
            "id": 1,
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2010,
            "color": "blanco",
            "license_plate": "AD12TW",
            "seats": 4
        },
        "condition": "PS",
        "price": "1234.00",
        "seats": 24
    }
]
```

**Detail demands:**

GET /demands/1/

**Response:**

```
{
    "id": 4,
    "departure_date": "2017-09-09T18:30:00+0000",
    "arrival_date": "2017-09-09T19:30:00+0000",
    "departure_address": {
        "latitude": "192.168.32.12",
        "longitude": "168.169.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "arrival_address": {
        "latitude": "192.168.30.13",
        "longitude": "168.158.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "condition_display": "Por puesto",
    "condition": "PS",
    "seats": 24
}
```

status = 200
----

PUT /demands/1/


**Request:**

```
{
    "accepted_offer_id": 24
}
```

**Response:**

```
{
    "id": 4,
    "departure_date": "2017-09-09T18:30:00+0000",
    "arrival_date": "2017-09-09T19:30:00+0000",
    "departure_address": {
        "latitude": "192.168.32.12",
        "longitude": "168.169.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "arrival_address": {
        "latitude": "192.168.30.13",
        "longitude": "168.158.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "condition_display": "Por puesto",
    "condition": "PS",
    "seats": 24,
    "offers": [
                    {
                    "id": 4,
                    "departure_date": "2017-09-09T18:30:00+0000",
                    "arrival_date": "2017-09-09T19:30:00+0000",
                    "departure_address": {
                        "latitude": "192.168.32.12",
                        "longitude": "168.169.23.21",
                        "text": "calle 5 de julio con av delicias"
                    },
                    "arrival_address": {
                        "latitude": "192.168.30.13",
                        "longitude": "168.158.23.21",
                        "text": "calle 5 de julio con av delicias"
                    },
                    "condition_display": "Por puesto",
                    "vehicle": {
                        "id": 1,
                        "brand": "Toyota",
                        "model": "Corolla",
                        "year": 2010,
                        "color": "blanco",
                        "license_plate": "AD12TW",
                        "seats": 4
                    },
                    "condition": "PS",
                    "price": "1234.00",
                    "seats": 24
                },
        ,...
    ]
}
```

status = 200