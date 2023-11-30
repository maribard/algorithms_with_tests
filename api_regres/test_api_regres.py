import pytest
import requests
from api_regres.checkers.checker_methods import check_headers, check_body, check_body_for_user_id


# GET /users
@pytest.mark.parametrize('per_page', [6])
def test_get_users_response_params_with_default_data(expected_response, per_page):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    response = requests.get('https://reqres.in/api/users')
    response_dict = response.json()

    assert response.status_code == 200
    assert len(response_dict['data']) == per_page
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body,
               expected_response_spec_data=expected_response_specific_data, index=0)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize('per_page', [2])
def test_get_users_response_params_with_default_page_param(expected_response, per_page, get_mock_db_connection):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    total_users = get_mock_db_connection.get_total_amount_of_users()
    response = requests.get(f'https://reqres.in/api/users?per_page={per_page}')
    response_dict = response.json()

    expected_response_body['per_page'] = per_page
    expected_response_body['total_pages'] = total_users / per_page

    assert len(response_dict['data']) == per_page
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body,
               expected_response_spec_data=expected_response_specific_data, index=0)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize('page, per_page', [(2, 6)])
def test_get_users_response_params_with_default_per_page_param(expected_response, page, per_page):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    response = requests.get(f'https://reqres.in/api/users?page={page}')
    response_dict = response.json()

    expected_response_body['page'] = page

    assert len(response_dict['data']) == per_page
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize("page, per_page", [(1, 1)])
def test_get_users_response_for_min_page_and_min_per_page(expected_response, page, per_page, get_mock_db_connection):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    total_users = get_mock_db_connection.get_total_amount_of_users()

    response = requests.get(f'https://reqres.in/api/users?page={page}&per_page={per_page}')
    response_dict = response.json()

    expected_response_body['page'] = page
    expected_response_body['per_page'] = per_page
    expected_response_body['total'] = total_users
    expected_response_body['total_pages'] = total_users

    assert len(response_dict['data']) == per_page
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body,
               expected_response_spec_data=expected_response_specific_data, index=0)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize("page", [1])
def test_get_users_response_for_min_page_and_max_per_page(expected_response, page, get_mock_db_connection):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    total_users = get_mock_db_connection.get_total_amount_of_users()

    response = requests.get(f'https://reqres.in/api/users?page={page}&per_page={total_users}')
    response_dict = response.json()

    expected_response_body['per_page'] = total_users
    expected_response_body['total'] = total_users
    expected_response_body['total_pages'] = page

    assert len(response_dict['data']) == total_users
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body,
               expected_response_spec_data=expected_response_specific_data, index=0)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize("per_page", [1])
def test_get_users_response_for_max_page_and_min_per_page(expected_response, per_page, get_mock_db_connection):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    total_users = get_mock_db_connection.get_total_amount_of_users()
    page = total_users

    response = requests.get(f'https://reqres.in/api/users?page={page}&per_page={per_page}')
    response_dict = response.json()

    expected_response_body['page'] = page
    expected_response_body['total'] = total_users
    expected_response_body['total_pages'] = total_users
    expected_response_body['per_page'] = per_page

    assert len(response_dict['data']) == per_page
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body)
    assert response.elapsed.total_seconds() < 0.2


def test_get_users_response_for_max_page_and_max_per_page(expected_response, get_mock_db_connection):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    total_users = get_mock_db_connection.get_total_amount_of_users()
    page = total_users

    response = requests.get(f'https://reqres.in/api/users?page={page}&per_page={total_users}')
    response_dict = response.json()

    expected_response_body['page'] = page
    expected_response_body['total_pages'] = 1
    expected_response_body['total'] = total_users
    expected_response_body['per_page'] = total_users

    assert len(response_dict['data']) == 0
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize("page, per_page", [("ytyt", "ko")])
def test_get_users_response_incorect_params(expected_response, page, per_page):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    response = requests.get(f'https://reqres.in/api/users?page={page}&per_page={per_page}')
    response_dict = response.json()

    assert len(response_dict['data']) == 6
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body,
               expected_response_spec_data=expected_response_specific_data, index=0)
    assert response.elapsed.total_seconds() < 0.2


def test_get_users_response_incorect_name_of_params(expected_response):
    expected_response_headers, expected_response_body, expected_response_specific_data = expected_response
    response = requests.get('https://reqres.in/api/uss?pae=ytyt&per_pge=ko')
    response_dict = response.json()

    assert len(response_dict['data']) == 6
    check_headers(response.headers, expected_response_headers)
    check_body(response_dict, expected_response_body)
    assert response.elapsed.total_seconds() < 0.2


# GET /users/{id}
@pytest.mark.parametrize("id", [1])
def test_get_users_id_response(expected_response_for_user_id, id):
    expected_response_headers, expected_response_body = expected_response_for_user_id
    response = requests.get(f'https://reqres.in/api/users/{id}')
    response_dict = response.json()
    assert response.status_code == 200
    assert len(response_dict) == 2
    assert len(response_dict['data']) == 5
    check_headers(response.headers, expected_response_headers)
    check_body_for_user_id(response_dict, expected_response_body)
    assert response.elapsed.total_seconds() < 0.2


@pytest.mark.parametrize("id", [0, "tyu"])
def test_get_users_id_response_incorect_int_param(id):
    response = requests.get(f'https://reqres.in/api/users/{id}')
    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 0.2


# PUT /users/{id}
@pytest.mark.parametrize("id", [1, '', 0])
def test_put_users_id_(id):
    response = requests.put(f'https://reqres.in/api/users/{id}')
    response_dict = response.json()
    assert response.status_code == 200
    assert 'updatedAt' in response_dict
    assert type(response_dict['updatedAt']) is str


# PATCH /users/{id}
@pytest.mark.parametrize("id", [1, '', 0])
def test_patch_users_id_(id):
    response = requests.patch(f'https://reqres.in/api/users/{id}')
    response_dict = response.json()
    assert response.status_code == 200
    assert 'updatedAt' in response_dict
    assert type(response_dict['updatedAt']) is str


# DELETE /users/{id}
@pytest.mark.parametrize("id", [1, '', 0])
def test_delete_users_id_(id):
    response = requests.delete(f'https://reqres.in/api/users/{id}')
    assert response.status_code == 204
    assert len(response.text) == 0
