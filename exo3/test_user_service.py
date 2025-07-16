import pytest


@pytest.fixture
def generate_password():
    with patch('user_service.generate_password', return_value='Password1'):
        yield