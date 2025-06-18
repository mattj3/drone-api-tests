import pytest
from utils import generate_valid_payload, generate_invalid_payloads

def test_generate_valid_payload_structure():
    payload = generate_valid_payload()
    assert set(payload.keys()) == {"lat", "lon", "alt", "speed", "heading"}
    assert isinstance(payload["lat"], float)
    assert isinstance(payload["lon"], float)
    assert isinstance(payload["alt"], int)
    assert isinstance(payload["speed"], int)
    assert isinstance(payload["heading"], int)

def test_invalid_payload_1():
    payload = generate_invalid_payloads()[0]
    assert "lat" in payload and not isinstance(payload["lat"], float)
    assert "lon" in payload and payload["lon"] is None
    assert "alt" in payload and not isinstance(payload["alt"], int)

def test_invalid_payload_2():
    payload = generate_invalid_payloads()[1]
    assert payload["lat"] > 90 or payload["lat"] < -90
    assert payload["lon"] < -180
    assert payload["alt"] < 0
    assert payload["speed"] < 0
    assert payload["heading"] > 360

def test_invalid_payload_3():
    payload = generate_invalid_payloads()[2]
    assert "alt" not in payload
    assert "speed" not in payload
    assert "heading" not in payload

def test_invalid_payload_4():
    payload = generate_invalid_payloads()[3]
    assert isinstance(payload["heading"], str)
