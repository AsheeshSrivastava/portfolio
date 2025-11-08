"""Quick API test to identify 500 errors."""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("=" * 60)
print("Testing Python Research Portal API")
print("=" * 60)

# Test 1: Health Check
print("\n1. Testing Health Endpoint...")
try:
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    assert response.status_code == 200
    print("   [OK] PASS")
except Exception as e:
    print(f"   [FAIL] FAIL: {e}")

# Test 2: List Documents
print("\n2. Testing List Documents...")
try:
    response = requests.get(f"{BASE_URL}/api/documents?limit=5")
    print(f"   Status: {response.status_code}")
    docs = response.json()
    print(f"   Documents found: {len(docs)}")
    assert response.status_code == 200
    print("   [OK] PASS")
except Exception as e:
    print(f"   [FAIL] FAIL: {e}")

# Test 3: Chat Query (This is likely where the 500 error occurs)
print("\n3. Testing Chat Query...")
try:
    payload = {
        "question": "What are Python functions?",
        "provider": "openai",
        "secret_token": None,
        "history": []
    }
    
    print(f"   Sending request...")
    response = requests.post(
        f"{BASE_URL}/api/chat/query",
        json=payload,
        timeout=30
    )
    
    print(f"   Status: {response.status_code}")
    
    if response.status_code == 500:
        print(f"   [ERROR] 500 ERROR DETECTED!")
        print(f"   Response Text: {response.text}")
        try:
            error_detail = response.json()
            print(f"   Error JSON: {json.dumps(error_detail, indent=2)}")
        except Exception as parse_err:
            print(f"   Could not parse JSON: {parse_err}")
    elif response.status_code == 200:
        result = response.json()
        print(f"   Answer length: {len(result.get('answer', ''))}")
        print(f"   Citations: {len(result.get('citations', []))}")
        print("   [OK] PASS")
    else:
        print(f"   [WARN] Unexpected status: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
        
except requests.exceptions.Timeout:
    print(f"   [FAIL] Request timed out")
except Exception as e:
    print(f"   [FAIL] FAIL: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("Test Complete")
print("=" * 60)

