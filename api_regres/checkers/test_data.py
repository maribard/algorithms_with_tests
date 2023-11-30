expected_response_headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Vary': 'Accept-Encoding',
    'Server': 'cloudflare'
}

expected_response_body = {
    "page": 1,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

expected_response_specific_data = {
    "id": 1,
    "email": "george.bluth@reqres.in",
    "first_name": "George",
    "last_name": "Bluth",
    "avatar": "https://reqres.in/img/faces/1-image.jpg"
}