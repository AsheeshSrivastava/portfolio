"""Test the research graph directly with full error output."""

import asyncio
import sys
import io
import traceback

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

async def test_graph():
    """Test the research graph."""
    print("\n" + "="*60)
    print("TESTING RESEARCH GRAPH")
    print("="*60 + "\n")
    
    try:
        print("[1/5] Importing dependencies...")
        from app.db.session import get_async_session_maker
        from app.security.secret_store import SecretStore
        from app.graph.research_graph import ResearchGraph
        from app.providers.base import ProviderName
        print("[OK] Imports successful\n")
        
        print("[2/5] Creating database session...")
        async_session_maker = get_async_session_maker()
        async with async_session_maker() as session:
            print("[OK] Database session created\n")
            
            print("[3/5] Creating secret store...")
            secret_store = SecretStore()
            print("[OK] Secret store created\n")
            
            print("[4/5] Creating ResearchGraph...")
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider=ProviderName.OPENAI,
                secret_token=None,
            )
            print("[OK] ResearchGraph created\n")
            
            print("[5/5] Running query...")
            initial_state = {
                "question": "What is print?",
                "history": [],
                "provider": "openai",
                "retry_count": 0,
            }
            
            print("Invoking graph...")
            result = await graph.graph.ainvoke(initial_state)
            
            print("\n" + "="*60)
            print("RESULT")
            print("="*60)
            print(f"Answer length: {len(result.get('answer', ''))} characters")
            print(f"Citations: {len(result.get('citations', []))}")
            print(f"Evaluation: {result.get('evaluation', {}).get('total_score', 'N/A')}")
            print("="*60 + "\n")
            
    except Exception as e:
        print("\n" + "="*60)
        print("ERROR")
        print("="*60)
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        print("="*60 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test_graph())



