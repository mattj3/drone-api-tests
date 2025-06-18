# drone-api-tests

## Mock Drone Telemetry API

A FastAPI-powered testbed for simulating drone telemetry data, used for developing and validating API test automation.

## File Structure

```
mock-drone-api/
├── app/
|   ├── __init__.py
│   └── app.py
│
├── tests/
|   ├── __init__.py
│   └── test_api.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Startup Steps

```bash
# 1. Create and activate virtualenv (if needed)
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Start API server
uvicorn app.app:app --reload

# 4. In another terminal, run tests
cd /to/repo/
source venv/bin/activate # as needed
pytest

```
