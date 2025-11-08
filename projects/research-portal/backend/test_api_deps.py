"""Test API dependencies."""

import asyncio
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test():
    print("\n[TEST] Testing API dependencies...")
    
    try:
        from app.db.dependencies import get_db_session
        from app.security.dependencies import get_secret_store_dependency
        from app.graph.research_graph import ResearchGraph
        
        print("[1/3] Getting database session...")
        async for session in get_db_session():
            print("[OK] Database session obtained")
            
            print("\n[2/3] Getting secret store...")
            secret_store = get_secret_store_dependency()
            print("[OK] Secret store obtained")
            
            print("\n[3/3] Creating ResearchGraph...")
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider="openai",
                secret_token=None,
            )
            print("[OK] ResearchGraph created successfully")
            
            print("\n[SUCCESS] All dependencies work!")
            break
            
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())



