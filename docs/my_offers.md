
**Offer:**

**Create Offer:**

**url:**

POST /my-offers/

**Request:**

```
{
    "departure_address": {
        "latitude": "192.168.32.12",
        "longitude": "168.169.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "departure_date": "2017-09-09T14:30:00-04:00",
    "arrival_date": "2017-09-09T15:30:00-04:00",
    "arrival_address": {
        "latitude": "192.168.30.13",
        "longitude": "168.158.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "vehicle_id": 1,
    "seats": 24,
    "condition": "PS",
    "price": 1234
}
```

**Response:**

status = 201

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

```

**List my offers:**

GET /my-offers/

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

**Detail my offers:**

GET /my-offers/1/

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
    "seats": 24,
    "seats": 24,
    "request_offer": [
        {
            "id": 1,
            "date": "2017-09-09T18:30:00+0000",
            "text": "texto"
        }
    ]
}
```

status = 200

**Update my offers:**

PUT /my-offers/1/

**Request:**

```
{
    "departure_address": {
        "latitude": "192.168.32.12",
        "longitude": "168.169.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "departure_date": "2017-09-09T14:30:00-04:00",
    "arrival_date": "2017-09-09T15:30:00-04:00",
    "arrival_address": {
        "latitude": "192.168.30.13",
        "longitude": "168.158.23.21",
        "text": "calle 5 de julio con av delicias"
    },
    "vehicle_id": 1,
    "seats": 24,
    "condition": "PS",
    "price": 1234
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
    "seats": 24,
    "request_offer": [
        {
            "id": 1,
            "date": "2017-09-09T18:30:00+0000",
            "text": "texto"
        }
    ]
}
```

status = 200


**Destroy vehicle:**

DELETE /my-offers/1/

satus = 204

**acceptar una oferta:**

POST /my-offers/1/accept-request/

**Response:**

```
{
    "detail": "accepted"
}
```

status = 201
