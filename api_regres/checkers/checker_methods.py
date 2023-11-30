def check_headers(present_response, expected_response):
    for key, value in present_response.items():
        if key in expected_response:
            assert value == expected_response[key]


def check_body(present_response, expected_response, expected_response_spec_data={}, index=0):
    for key, value in present_response.items():
        if type(value) is not list:
            assert value == expected_response[key]
        elif type(value) is list:
            for user in value:
                assert type(user['id']) is int
                assert type(user['email']) is str
                assert type(user['first_name']) is str
                assert type(user['last_name']) is str
                assert type(user['avatar']) is str

    if expected_response_spec_data:
        for key, value in present_response['data'][index].items():
            assert value == expected_response_spec_data[key]


def check_body_for_user_id(present_response, expected_response):
    for key, value in present_response.items():
        for key1, value1 in value.items():
            assert value1 == expected_response[key][key1]
