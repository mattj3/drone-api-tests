# Test Plan – mock‑drone‑api‑testing

## 1. Overview

This document defines the strategy for testing the Mock Drone API—an async FastAPI service simulating drone telemetry endpoints. Our goal is to ensure correctness of request handling, data storage, error paths, and utility functions.

## 2. Scope

- **API Endpoints**
  - `POST /telemetry` – Create a new flight session
  - `GET  /flight/{flight_id}` – Retrieve flight telemetry
  - `POST /telemetry/{flight_id}` – Append data to an existing flight
  - `DELETE /reset` – Reset in‑memory storage
- **Utility Functions**
  - Payload generators in `utils.py`
- **Test Suites**
  - Unit tests for helpers
  - Integration tests for endpoint sequences
  - Negative tests for invalid inputs

## 3. Test Types

| Type            | Location                     | Purpose                                                         |
| --------------- | ---------------------------- | --------------------------------------------------------------- |
| **Unit**        | `tests/test_unit_utils.py`   | Validate `utils.py` functions generate correct payload shapes   |
| **Integration** | `tests/test_positive_api.py` | Exercise happy‑path flows (create → append → fetch)             |
| **Negative**    | `tests/test_negative_api.py` | Assert proper error responses on malformed or out‑of‑scope data |

## 4. Tools & Frameworks

- **pytest** – test runner
- **httpx** – async HTTP client for exercising endpoints
- **pytest‑asyncio** – async test support
- **pytest‑html** (optional) – generate HTML test reports

## 5. Environments

- **Local** – FastAPI via Uvicorn/local mock data
- **CI Pipeline** – GitHub Actions (runs `pytest --maxfail=1 --disable-warnings -q`)

## 6. Test Data

- **Valid payloads**
  - GPS coordinates (lat, lon in correct ranges)
  - Timestamps in ISO 8601
- **Invalid payloads**
  - Missing fields (e.g. no `lat`)
  - Bad types (e.g. string instead of float)
  - Out‑of‑range values (e.g. lat > 90)
  - Nonexistent `flight_id` on append

## 7. Test Cases (Summary)

| Endpoint                 | Method | Scenario                      | Expected Result                   |
| ------------------------ | ------ | ----------------------------- | --------------------------------- |
| `/telemetry`             | POST   | Valid payload                 | 201 + JSON `{ "flight_id": ... }` |
|                          |        | Missing required field        | 422 Unprocessable Entity          |
|                          |        | Bad data types                | 422                               |
| `/flight/{flight_id}`    | GET    | Existing flight               | 200 + telemetry array             |
|                          |        | Unknown `flight_id`           | 404 Not Found                     |
| `/telemetry/{flight_id}` | POST   | Valid append                  | 200 + updated telemetry           |
|                          |        | Append to unknown `flight_id` | 404 Not Found                     |
|                          |        | Malformed body                | 422                               |
| `/reset`                 | DELETE | Always                        | 204 No Content (state cleared)    |

## 8. Reporting & Metrics

- **Coverage**: aim for ≥ 90% on both `app.py` and `utils.py`
- **Test Duration**: keep full suite under 10s locally

## 9. Out of Scope

- Load/performance testing
- Authentication/security checks
- Front‑end or real hardware integration

## 10. Future Work

- Add **load tests** (e.g., via Locust)
- Extend API with auth and rate‑limiting scenarios
- Automate **contract tests** against an OpenAPI spec
