"""Simple test for compiler pipeline."""

import asyncio
import sys
import io

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

async def test():
    print("\n[TEST] Testing compiler imports and initialization...")
    
    try:
        from app.core.config import get_settings
        settings = get_settings()
        print(f"[OK] Settings loaded")
        print(f"  - enable_technical_compiler: {settings.enable_technical_compiler}")
        print(f"  - compiler_quality_threshold: {settings.compiler_quality_threshold}")
        print(f"  - compiler_temperature: {settings.compiler_temperature}")
        
        from app.graph.technical_compiler import TechnicalCompiler
        compiler = TechnicalCompiler()
        print(f"[OK] TechnicalCompiler initialized")
        
        from app.quality.compiler_evaluator import CompilerQualityEvaluator
        evaluator = CompilerQualityEvaluator()
        print(f"[OK] CompilerQualityEvaluator initialized")
        
        # Test compilation
        print("\n[TEST] Testing compilation...")
        technical_answer = "Anaconda is a Python distribution. [doc-1]"
        citations = [{"id": "doc-1", "source": "Test"}]
        
        compiled = await compiler.compile(technical_answer, citations)
        print(f"[OK] Compilation successful")
        print(f"  Length: {len(compiled)} chars")
        
        # Test evaluation
        print("\n[TEST] Testing evaluation...")
        evaluation = evaluator.evaluate(compiled, technical_answer)
        print(f"[OK] Evaluation successful")
        print(f"  Score: {evaluation.total_score}")
        print(f"  Passed: {evaluation.passed}")
        
        print("\n[SUCCESS] All tests passed!")
        
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test())



