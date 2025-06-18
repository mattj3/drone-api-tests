from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict
import uuid

app = FastAPI(title="Mock Drone Telemetry API")

# In-memory store
_flights: Dict[str, dict] = {}

# --- Models ---
class Telemetry(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    alt: float = Field(..., ge=0)
    speed: float = Field(..., ge=0)
    heading: float = Field(..., ge=0, le=360)

class FlightResponse(BaseModel):
    flight_id: str
    data: list[Telemetry]

# --- Endpoints ---
@app.post("/telemetry", response_model=dict, status_code=status.HTTP_201_CREATED)
def post_telemetry(data: Telemetry):
    flight_id = str(uuid.uuid4())
    _flights[flight_id] = [data.model_dump()]
    return {"flight_id": flight_id, "status": "ok"}

@app.get("/flight/{flight_id}", response_model=FlightResponse)
def get_flight_data(flight_id: str):
    if flight_id not in _flights:
        raise HTTPException(status_code=404, detail="Flight ID not found")
    return {"flight_id": flight_id, "data": _flights[flight_id]}

@app.post("/telemetry/{flight_id}", response_model=dict, status_code=status.HTTP_201_CREATED)
def append_telemetry(flight_id: str, data: Telemetry):
    if flight_id not in _flights:
        raise HTTPException(status_code=404, detail="Flight ID not found")
    _flights[flight_id].append(data.model_dump())
    return {"flight_id": flight_id, "status": "appended"}

@app.delete("/reset", response_model=dict)
def reset():
    _flights.clear()
    return {"status": "reset"}
