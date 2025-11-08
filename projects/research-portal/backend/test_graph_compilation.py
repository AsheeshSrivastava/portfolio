"""Test graph compilation to find the error."""

import asyncio
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

async def test():
    print("\n[TEST] Testing graph compilation...")
    
    try:
        print("[1/4] Importing database...")
        from app.db.session import database
        
        print("[2/4] Importing ResearchGraph...")
        from app.graph.research_graph import ResearchGraph
        from app.security.secret_store import SecretStore
        
        print("[3/4] Creating graph instance...")
        async with database.session() as session:
            secret_store = SecretStore()
            
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider="openai",
                secret_token=None,
            )
            
            print("[4/4] Graph created successfully!")
            print(f"  - Technical compiler enabled: {graph.technical_compiler is not None}")
            print(f"  - Compiler evaluator enabled: {graph.compiler_evaluator is not None}")
            
            print("\n[SUCCESS] Graph compilation successful!")
            
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test())



