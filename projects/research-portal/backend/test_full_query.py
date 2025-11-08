"""Test full query execution to find the error."""

import asyncio
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix for Windows async psycopg compatibility
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test():
    print("\n[TEST] Testing full query execution...")
    
    try:
        from app.db.session import database
        from app.graph.research_graph import ResearchGraph
        from app.security.secret_store import SecretStore
        
        print("[1/3] Creating graph...")
        async with database.session() as session:
            secret_store = SecretStore()
            
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider="openai",
                secret_token=None,
            )
            
            print("[2/3] Running query...")
            result = await graph.run(
                question="What is print in Python?",
                history=[],
            )
            
            print("[3/3] Query completed!")
            print(f"  - Answer length: {len(result.get('answer', ''))} chars")
            print(f"  - Compiled answer length: {len(result.get('compiled_answer', ''))} chars")
            print(f"  - Quality score: {result.get('evaluation', {}).get('total_score', 'N/A')}")
            
            print("\n[SUCCESS] Full query execution successful!")
            
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test())

