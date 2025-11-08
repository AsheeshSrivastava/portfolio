"""Debug the chat endpoint directly."""

import asyncio
import sys
import json

# Fix for Windows async psycopg compatibility
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("=" * 60)
print("Testing Chat Endpoint Directly")
print("=" * 60)

payload = {
    "question": "What is Python?",
    "provider": "openai",
    "secret_token": None,
    "history": []
}

print("\nSending request...")
print(f"Payload: {json.dumps(payload, indent=2)}")

try:
    response = client.post("/api/chat/query", json=payload)
    print(f"\nStatus: {response.status_code}")
    
    if response.status_code == 200:
        print("[OK] Success!")
        result = response.json()
        print(f"Answer length: {len(result.get('answer', ''))}")
        print(f"Citations: {len(result.get('citations', []))}")
        print(f"Evaluation: {result.get('evaluation', {})}")
    else:
        print(f"[ERROR] Failed with status {response.status_code}")
        print(f"Response: {response.text}")
        try:
            error_detail = response.json()
            print(f"Error JSON: {json.dumps(error_detail, indent=2)}")
        except:
            pass
except Exception as e:
    print(f"[ERROR] Exception: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)




