import pytest
from httpx import AsyncClient, ASGITransport
from app.app import app
from utils import generate_valid_payload

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_post_telemetry():
    payload = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/telemetry", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert "flight_id" in data
        assert data["status"] == "ok"

@pytest.mark.asyncio
async def test_get_flight_data():
    payload = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        post_response = await ac.post("/telemetry", json=payload)
        flight_id = post_response.json()["flight_id"]

        get_response = await ac.get(f"/flight/{flight_id}")
        assert get_response.status_code == 201
        flight_data = get_response.json()
        assert flight_data["flight_id"] == flight_id
        assert len(flight_data["data"]) == 1

@pytest.mark.asyncio
async def test_append_telemetry():
    initial_payload = generate_valid_payload()
    append_payload = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        post_response = await ac.post("/telemetry", json=initial_payload)
        flight_id = post_response.json()["flight_id"]

        append_response = await ac.post(f"/telemetry/{flight_id}", json=append_payload)
        assert append_response.status_code == 201
        assert append_response.json()["status"] == "appended"

        get_response = await ac.get(f"/flight/{flight_id}")
        assert len(get_response.json()["data"]) == 2

@pytest.mark.asyncio
async def test_delete_reset():
    payload = generate_valid_payload()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        await ac.post("/telemetry", json=payload)

        reset_response = await ac.delete("/reset")
        assert reset_response.status_code == 200
        assert reset_response.json()["status"] == "reset"
