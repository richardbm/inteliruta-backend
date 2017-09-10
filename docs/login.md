
**Login y signup para usuarios y administrador**


**Login Admin:**

El login es con username y password

El usuario por defecto es

user: 4geeks
pass: 4geeks1o1

**url:**

POST /accounts/login-admin/

**Request:**

```
{
    "username": "4geeks",
    "password": "4geeks1o1*"
}
```

**Response:**

status = 200

```
{
    "token": "87wdfe87fhw8efh8wef43f"
}
```

**Login Con Facebook:**

El login en esta app solo se realiza con Facebook


cuando se envia el campo signup: false solo permite realizar login, no registro

se usa para verificar si un usuario se ha registrado o no.


** Admin Web:**

**url:**

POST /accounts/signup-facebook/

**Request:**

```
{
    "code": "34234234234534",
    "redirectUri": "http://45.77.73.99:8000/",
    "signup": true
}
```

**Response:**

status = 200

```
{
    "token": "87wdfe87fhw8efh8wef43f"
    "registered": true
}
```

en esta API, de ser satisfactorio el registro, el campo "registered" siempre retornará un valor "true"

**APP mobile:**

**url:**

POST /mobile/accounts/signup-facebook/

**Request:**

```
{
    "access_token": "34234234234534",
    "redirectUri": "http://45.77.73.99:8000/",
    "signup": true
}
```

**Response:**

status = 200

```
{
    "token": "87wdfe87fhw8efh8wef43f"
    "registered": true
}
```

en esta API, de ser satisfactorio el registro, el campo "registered" siempre retornará un valor "true"