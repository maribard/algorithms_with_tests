import pytest
from api_regres.db_client import DBClient

@pytest.fixture
def expected_response():
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

    return expected_response_headers, expected_response_body, expected_response_specific_data


@pytest.fixture
def get_mock_db_connection():
    client = DBClient()
    return client


@pytest.fixture
def expected_response_for_user_id():
    expected_response_headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Vary': 'Accept-Encoding',
        'Server': 'cloudflare'
    }

    expected_response_body = {
        "data": {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

    return expected_response_headers, expected_response_body