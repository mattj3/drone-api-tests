# mock-drone-api-testing

![Drone API Tests](https://github.com/mattj3/drone-api-tests/actions/workflows/ci.yml/badge.svg)
[![Test Plan](https://img.shields.io/badge/docs-test--plan-blue)](./test_plan.md)

**Mock Drone API Testing** is a lightweight FastAPI service that simulates basic drone telemetry endpoints. It’s built as a testing sandbox for QA engineers and developers to practice API automation by sending mock GPS data, appending flight logs, and resetting server state.

This project is ideal for:

- Writing and validating API test cases with `pytest` and `httpx`
- Testing edge cases like missing or malformed telemetry
- Practicing CI/CD integration using GitHub Actions or other tools

## Features

- REST API endpoints to post and retrieve drone telemetry data
- In-memory storage simulating drone flight sessions
- Supports appending telemetry data to existing flights
- Reset endpoint to clear stored data
- Fully async test suite using **pytest** and **httpx** for thorough validation
- Payload generation utilities for both valid and invalid test scenarios

## File Structure

```plaintext
mock-drone-api-testing/
├── app/
│   ├── __init__.py
│   └── app.py              # FastAPI app with endpoints and data models
│
├── tests/
│   ├── __init__.py
│   ├── test_negative_api.py  # Negative scenario tests (async)
│   ├── test_positive_api.py  # Positive scenario tests (async)
│   └── test_unit_utils.py    # Unit tests for payload generators
│
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt         # Python dependencies
├── test_plan.md             # Project test plan
└── utils.py                 # Helper functions for payload generation
```

## Setup and Run

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```bash
uvicorn app.app:app --reload
```

The API will be running at: http://127.0.0.1:8000

### 4. Run tests (in another terminal)

```bash
pytest
```

## API Endpoints

| Method | Endpoint                 | Description                                                 |
| ------ | ------------------------ | ----------------------------------------------------------- |
| POST   | `/telemetry`             | Create new flight with telemetry data (returns `flight_id`) |
| GET    | `/flight/{flight_id}`    | Retrieve all telemetry for a flight                         |
| POST   | `/telemetry/{flight_id}` | Append telemetry data to existing flight                    |
| DELETE | `/reset`                 | Clear all stored flight data (for test resets)              |

## API Documentation

Once the server is running, access the interactive API docs at: http://127.0.0.1:8000/docs
