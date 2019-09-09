from main import get_temperature
import pytest

def test_get_temperature_by_lat_lng():
    result = get_temperature(-14.235004, -51.92528)
    # with pytest.raises(16):
    #     get_temperature(-14.235004, -51.92528)
    assert result == 36
    # raise NotImplementedError
