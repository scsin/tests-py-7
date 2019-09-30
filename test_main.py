from main import get_temperature
import pytest
import requests
from unittest.mock import Mock

class MockResponse:
    @staticmethod
    def json():
        return {"currently": {"temperature": 62}}

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse.json()

    monkeypatch.setattr(requests, "get", mock_get)

def test_get_temperature_by_lat_lng(mock_response):
    result = get_temperature(-14.235004, -51.92528)
    assert result == 16

test_get_temperature_by_lat_lng(mock_response)