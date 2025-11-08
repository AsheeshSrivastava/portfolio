"""Test if the graph can be built."""

import asyncio
import sys
import io

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

async def test():
    print("\n[TEST] Testing graph building...")
    
    try:
        from app.db.session import database
        from app.security.secret_store import SecretStore
        from app.graph.research_graph import ResearchGraph
        from app.providers.base import ProviderName
        
        print("[OK] Imports successful")
        
        # Initialize database
        database.configure()
        print("[OK] Database configured")
        
        # Create session
        async with database.session() as session:
            print("[OK] Database session created")
            
            # Create secret store
            secret_store = SecretStore()
            print("[OK] Secret store created")
            
            # Try to create ResearchGraph
            print("\n[TEST] Creating ResearchGraph...")
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider="openai",  # ProviderName is a Literal type, not an enum
                secret_token=None,
            )
            print("[OK] ResearchGraph created successfully!")
            
            # Try to run a simple query
            print("\n[TEST] Running simple query...")
            result = await graph.run(
                question="What is print?",
                history=[],
            )
            
            print("[OK] Query completed!")
            print(f"  Answer length: {len(result.get('answer', ''))} chars")
            print(f"  Compiled answer length: {len(result.get('compiled_answer', ''))} chars")
            
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test())

