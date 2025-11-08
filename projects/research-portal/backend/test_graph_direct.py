"""Direct test of ResearchGraph to identify the issue."""

import asyncio
import sys
from pathlib import Path

# Fix for Windows async psycopg compatibility
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from app.core.config import get_settings
from app.db.session import database
from app.graph.research_graph import ResearchGraph
from app.security.secret_store import SecretStore
from app.core.redis import get_redis


async def test_graph():
    """Test the research graph directly."""
    
    print("=" * 60)
    print("Testing ResearchGraph Directly")
    print("=" * 60)
    
    try:
        # Initialize database
        print("\n1. Initializing database...")
        database.configure()
        print("   [OK] Database configured")
        
        # Initialize Redis
        print("\n2. Initializing Redis...")
        redis_client = get_redis()
        await redis_client.ping()
        print("   [OK] Redis configured")
        
        # Create secret store
        print("\n3. Creating secret store...")
        secret_store = SecretStore(redis_client=redis_client)
        print("   [OK] Secret store created")
        
        # Create graph
        print("\n4. Creating ResearchGraph...")
        async with database.session() as session:
            try:
                graph = ResearchGraph(
                    session=session,
                    secret_store=secret_store,
                    provider="openai",
                    secret_token=None,
                )
                print("   [OK] Graph created successfully")
                
                # Test run
                print("\n5. Running graph with test question...")
                result = await graph.run(
                    question="What is Python?",
                    history=[],
                )
                print(f"   [OK] Graph executed")
                print(f"   Answer length: {len(result.get('answer', ''))}")
                print(f"   Answer preview: {result.get('answer', '')[:100]}...")
                print(f"   Citations: {len(result.get('citations', []))}")
                print(f"   Documents: {len(result.get('documents', []))}")
                
            except Exception as e:
                print(f"   [FAIL] Error during graph execution:")
                print(f"   {type(e).__name__}: {e}")
                import traceback
                traceback.print_exc()
                
    except Exception as e:
        print(f"\n[FAIL] Setup error:")
        print(f"{type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Test Complete")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_graph())

