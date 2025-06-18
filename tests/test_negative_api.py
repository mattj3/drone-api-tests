import pytest
from httpx import AsyncClient, ASGITransport
from app.app import app
from utils import generate_invalid_payloads, generate_valid_payload

transport = ASGITransport(app=app)

@pytest.mark.asyncio
@pytest.mark.parametrize("payload", generate_invalid_payloads())
async def test_post_telemetry_invalid_payload(payload):
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/telemetry", json=payload)
        assert response.status_code == 422

@pytest.mark.asyncio
@pytest.mark.parametrize("payload", generate_invalid_payloads())
async def test_append_telemetry_invalid_payload(payload):
    # First, create a valid flight to get a flight_id
    valid = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/telemetry", json=valid)
        flight_id = create_response.json()["flight_id"]

        # Now test invalid payload
        response = await ac.post(f"/telemetry/{flight_id}", json=payload)
        assert response.status_code == 422

@pytest.mark.asyncio
async def test_get_flight_data_invalid_id():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/flight/nonexistent-id")
        assert response.status_code == 404
        assert response.json()["detail"] == "Flight ID not found"

@pytest.mark.asyncio
async def test_append_telemetry_invalid_id():
    valid = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/telemetry/nonexistent-id", json=valid)
        assert response.status_code == 404
        assert response.json()["detail"] == "Flight ID not found"
