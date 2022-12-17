import pytest
from django.test import Client

@pytest.fixture
def Client():
    client = Client()
    return client