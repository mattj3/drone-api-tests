# Unit tests for utils.py functions
from app.utils import generate_valid_payload, generate_invalid_payload

def test_generate_valid_payload():
    payload = generate_valid_payload()
    
    assert isinstance(payload, dict)
    assert 'lat' in payload and isinstance(payload['lat'], float)
    assert -90 <= payload['lat'] <= 90

    assert 'lon' in payload and isinstance(payload['lon'], float)
    assert -180 <= payload['lon'] <= 180

    assert 'alt' in payload and isinstance(payload['alt'], int)
    assert 50 <= payload['alt'] <= 500

    assert 'speed' in payload and isinstance(payload['speed'], int)
    assert 1 <= payload['speed'] <= 100

    assert 'heading' in payload and isinstance(payload['heading'], int)
    assert 0 <= payload['heading'] <= 359

def test_generate_invalid_payload():
    payload = generate_invalid_payload()
    
    assert isinstance(payload, dict)
    assert 'lat' in payload and not isinstance(payload['lat'], float)
    assert 'lon' in payload and payload['lon'] is None
    assert 'alt' in payload and not isinstance(payload['alt'], int)

    # Assert speed and heading are missing from payload
    assert 'speed' not in payload
    assert 'heading' not in payload
