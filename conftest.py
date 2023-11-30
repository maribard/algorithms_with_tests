import pytest
from utils.file_reader import read_file

@pytest.fixture
def create_data():
    payload = read_file('strings_data.json')
    yield payload
