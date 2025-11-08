"""Minimal API test to isolate the issue."""

import asyncio
import sys
import io
import httpx

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test():
    print("\n[TEST] Testing API endpoint directly...")
    
    async with httpx.AsyncClient() as client:
        try:
            print("[1/2] Testing health endpoint...")
            response = await client.get("http://127.0.0.1:8000/api/health", timeout=5.0)
            print(f"[OK] Health: {response.status_code}")
            
            print("\n[2/2] Testing chat endpoint...")
            payload = {
                "question": "test",
                "provider": "openai",
                "history": []
            }
            response = await client.post(
                "http://127.0.0.1:8000/api/chat/query",
                json=payload,
                timeout=120.0
            )
            print(f"[RESPONSE] Status: {response.status_code}")
            print(f"[RESPONSE] Body: {response.text[:500]}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"[OK] Answer length: {len(result.get('answer', ''))}")
            else:
                print(f"[ERROR] Request failed")
            
        except httpx.HTTPStatusError as e:
            print(f"\n[ERROR] HTTP {e.response.status_code}")
            print(f"Response: {e.response.text}")
        except Exception as e:
            print(f"\n[ERROR] {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())

