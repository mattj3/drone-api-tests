import random

def generate_valid_payload():
    return {
        "lat": round(random.uniform(-90, 90), 6),
        "lon": round(random.uniform(-180, 180), 6),
        "alt": random.randint(50, 500),
        "speed": random.randint(1, 100),
        "heading": random.randint(0, 359)
    }

def generate_invalid_payload():
    return {
        "lat": "invalid_latitude",       # Should be a float
        "lon": None,                     # Missing value
        "alt": "high",                  # Should be an integer
        # Missing speed and heading
    }
