import pytest
import client

@pytest.fixture
def _client_fixture():
    return client.Client()