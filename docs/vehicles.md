
**Vehicles:**

**Create Vehicle:**

**url:**

POST /my-vehicles/

**Request:**

```
{
    "id": 1,
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2002,
    "color": "rojo",
    "license_plate": "AD34TD",
    "seats": 4
}
```

**Response:**

status = 201

```
{
    "id": 1,
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2002,
    "color": "rojo",
    "license_plate": "AD34TD",
    "seats": 4
}

```

**List my vehicles:**

GET /my-vehicles/

**Response:**

```
[
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2002,
        "color": "rojo",
        "license_plate": "AD34TD",
        "seats": 4
    }
]
```

**Detail my vehicles:**

GET /my-vehicles/1/

**Response:**

```
[
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2002,
        "color": "rojo",
        "license_plate": "AD34TD",
        "seats": 4
    }
]
```

status = 200


**Destroy vehicle:**

DELETE /my-vehicles/1/

satus = 204