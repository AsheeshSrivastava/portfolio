"""Test to see actual compiler output."""

import asyncio
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix for Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test():
    print("\n[TEST] Getting actual compiler output...")
    
    try:
        from app.db.session import database
        from app.graph.research_graph import ResearchGraph
        from app.security.secret_store import SecretStore
        
        async with database.session() as session:
            secret_store = SecretStore()
            
            graph = ResearchGraph(
                session=session,
                secret_store=secret_store,
                provider="openai",
                secret_token=None,
            )
            
            print("[RUNNING] Query...")
            result = await graph.run(
                question="What is print in Python?",
                history=[],
            )
            
            compiled = result.get('compiled_answer', '')
            
            print("\n" + "="*80)
            print("COMPILED OUTPUT:")
            print("="*80)
            print(compiled)
            print("="*80)
            
            # Check for sections
            print("\n[CHECKING] Required sections...")
            has_real_world = "### Real-World Examples" in compiled
            has_reflection = "### Reflection" in compiled
            consider_count = compiled.count("Consider")
            code_blocks = compiled.count("```")
            
            print(f"  Real-World Examples section: {'[OK]' if has_real_world else '[MISSING]'}")
            print(f"  Reflection section: {'[OK]' if has_reflection else '[MISSING]'}")
            print(f"  'Consider' prompts: {consider_count}")
            print(f"  Code blocks: {code_blocks}")
            
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())



