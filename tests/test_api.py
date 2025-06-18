from fastapi.testclient import TestClient
from app.app import app
from app.utils import generate_valid_payload

client = TestClient(app)

# Create new flight
def test_post_telemetry():
    payload = generate_valid_payload()
    try:
        response = client.post("/telemetry", json=payload)
        assert response.status_code == 201
        flight_id = response.json()["flight_id"]
        print(f"✅ POST /telemetry passed. Flight ID: {flight_id}")
    except AssertionError:
        print(f"❌ POST /telemetry failed. Status: {response.status_code}, Body: {response.text}")
        raise

# Get flight data
def test_get_flight_data():
    telemetry = generate_valid_payload()
    create_resp = client.post("/telemetry", json=telemetry)
    flight_id = create_resp.json()["flight_id"]

    try:
        get_resp = client.get(f"/flight/{flight_id}")
        assert get_resp.status_code == 200
        data = get_resp.json()
        print(f"✅ GET /flight/{flight_id} returned {len(data['data'])} telemetry entries")
    except AssertionError:
        print(f"❌ GET /flight/{flight_id} failed. Status: {get_resp.status_code}, Body: {get_resp.text}")
        raise

# Create new flight and append new telemetry data
def test_append_telemetry():
    initial_payload = generate_valid_payload()
    new_payload = generate_valid_payload()
    create_resp = client.post("/telemetry", json=initial_payload)
    flight_id = create_resp.json()["flight_id"]

    try:
        append_resp = client.post(f"/telemetry/{flight_id}", json=new_payload)
        assert append_resp.status_code == 201
        print(f"✅ POST /telemetry/{flight_id} append passed")

        get_resp = client.get(f"/flight/{flight_id}")
        data = get_resp.json()
        assert len(data['data']) == 2
        print(f"📡 GET /flight/{flight_id} confirms 2 telemetry entries")
    except AssertionError:
        print(f"❌ Append telemetry failed. Append status: {append_resp.status_code}, Body: {append_resp.text}")
        raise

# Clear all test flight data
def test_reset():
    try:
        response = client.delete("/reset")
        assert response.status_code == 200
        print("✅ DELETE /reset passed")
    except AssertionError:
        print(f"❌ DELETE /reset failed. Status: {response.status_code}, Body: {response.text}")
        raise
