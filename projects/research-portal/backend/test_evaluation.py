"""Test quality evaluation in chat endpoint."""

import asyncio
import json
from httpx import AsyncClient
from app.main import app


async def test_evaluation():
    """Test that evaluation data is properly returned."""
    print("=" * 60)
    print("Testing Quality Evaluation")
    print("=" * 60)
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/chat/query",
            json={
                "question": "What are Python functions?",
                "provider": "openai",
                "history": [],
            },
        )
        
        print(f"\nStatus: {response.status_code}")
        
        if response.status_code != 200:
            print(f"ERROR: {response.text}")
            return
        
        data = response.json()
        
        print(f"Has answer: {bool(data.get('answer'))}")
        print(f"Answer length: {len(data.get('answer', ''))}")
        print(f"Citations count: {len(data.get('citations', []))}")
        
        evaluation = data.get("evaluation", {})
        print(f"\nHas evaluation: {bool(evaluation)}")
        
        if evaluation:
            print(f"Evaluation keys: {list(evaluation.keys())}")
            print(f"\nTotal score: {evaluation.get('total_score')}")
            print(f"Passed: {evaluation.get('passed')}")
            print(f"Coverage score: {evaluation.get('coverage_score')}")
            print(f"Citation density: {evaluation.get('citation_density')}")
            print(f"Exec OK: {evaluation.get('exec_ok')}")
            print(f"Scope OK: {evaluation.get('scope_ok')}")
            print(f"Feedback count: {len(evaluation.get('feedback', []))}")
            print(f"Criteria count: {len(evaluation.get('criteria', {}))}")
            
            print("\n" + "=" * 60)
            print("Full Evaluation Data:")
            print("=" * 60)
            print(json.dumps(evaluation, indent=2))
        else:
            print("\n[ERROR] No evaluation data returned!")
        
        print("\n" + "=" * 60)
        print("Test Complete")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_evaluation())



