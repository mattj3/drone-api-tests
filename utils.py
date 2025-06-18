import random

def generate_valid_payload():
    return {
        "lat": round(random.uniform(-90, 90), 6),
        "lon": round(random.uniform(-180, 180), 6),
        "alt": random.randint(50, 500),
        "speed": random.randint(1, 100),
        "heading": random.randint(0, 359)
    }

def generate_invalid_payloads():
    return [
        {
            "lat": "invalid_latitude",       # Should be a float
            "lon": None,                     # Missing value
            "alt": "high",                  # Should be an integer
            # Missing speed and heading
        },
        {
            "lat": 200,                      # Out of range
            "lon": -181,                     # Out of range
            "alt": -10,                      # Negative altitude
            "speed": -5,                     # Negative speed
            "heading": 400                   # Heading out of range
        },
        {
            "lat": 45.0,
            "lon": 90.0,
            # Missing alt, speed, heading
        },
        {
            "lat": 45.0,
            "lon": 90.0,
            "alt": 100,
            "speed": 50,
            "heading": "east"               # Wrong type
        }
    ]
