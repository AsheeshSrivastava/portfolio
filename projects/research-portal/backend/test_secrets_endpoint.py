"""Test the secrets endpoint."""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("Testing /api/secrets endpoint...")

payload = {
    "provider": "openai",
    "api_key": "sk-test-key-12345",
    "ttl_seconds": 3600
}

try:
    response = requests.post(
        f"{BASE_URL}/api/secrets",
        json=payload,
        timeout=10
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"Success! Token: {result['token']}")
        print(f"Provider: {result['provider']}")
        print(f"Expires in: {result['expires_in']}s")
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Exception: {e}")




