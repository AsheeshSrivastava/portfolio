"""Quick test of multi-agent pipeline."""

import asyncio
import sys

from app.core.config import get_settings
from app.db.session import database
from app.graph.research_graph import ResearchGraph
from app.security.secret_store import SecretStore

# Fix for Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def test_pipeline():
    """Test the multi-agent pipeline with a simple question."""
    print("\n" + "="*80)
    print("TESTING MULTI-AGENT PIPELINE")
    print("="*80)
    
    settings = get_settings()
    print(f"\nSettings:")
    print(f"  Multi-agent pipeline: {settings.enable_multi_agent_pipeline}")
    print(f"  Narrative enrichment: {settings.enable_narrative_enrichment}")
    print(f"  Gemini key present: {bool(settings.google_api_key)}")
    
    # Create session
    async with database.session() as session:
        # Create secret store
        secret_store = SecretStore()
        
        # Create graph
        graph = ResearchGraph(
            session=session,
            secret_store=secret_store,
            provider="openai",
            secret_token=None,
        )
        
        print(f"\nGraph components:")
        print(f"  Complexity classifier: {graph.complexity_classifier is not None}")
        print(f"  Scenario architect: {graph.scenario_architect is not None}")
        print(f"  CoT storyteller: {graph.cot_storyteller is not None}")
        print(f"  Narrative evaluator: {graph.narrative_evaluator is not None}")
        print(f"  Aethelgard evaluator: {graph.aethelgard_evaluator is not None}")
        print(f"  Narrative enricher: {graph.narrative_enricher is not None}")
        
        # Test question
        question = "What is Anaconda?"
        print(f"\nTesting with question: {question}")
        print("Running pipeline...\n")
        
        # Run pipeline
        result = await graph.run(question=question, history=[])
        
        print("\n" + "="*80)
        print("RESULTS")
        print("="*80)
        
        # Check what we got
        print(f"\nComplexity: {result.get('complexity', 'NOT SET')}")
        print(f"Scenario present: {bool(result.get('scenario'))}")
        print(f"Story content present: {bool(result.get('story_content'))}")
        print(f"Enriched answer present: {bool(result.get('enriched_answer'))}")
        print(f"Enrichment applied: {result.get('enrichment_applied', False)}")
        print(f"Enrichment aborted: {result.get('enrichment_aborted', False)}")
        print(f"Abort reason: {result.get('abort_reason', 'N/A')}")
        
        # Check evaluations
        print(f"\nEvaluations:")
        tech_eval = result.get('evaluation', {})
        print(f"  Technical score: {tech_eval.get('total_score', 'N/A')}")
        
        narr_eval = result.get('narrative_evaluation', {})
        print(f"  Narrative score: {narr_eval.get('total_score', 'N/A')}")
        print(f"  Tech preservation: {narr_eval.get('technical_preservation', 'N/A')}")
        
        aeth_eval = result.get('aethelgard_evaluation', {})
        print(f"  Aethelgard score: {aeth_eval.get('total_score', 'N/A')}")
        print(f"  Brand voice: {aeth_eval.get('brand_voice', 'N/A')}")
        
        # Show answer preview
        answer = result.get('enriched_answer') or result.get('answer', '')
        print(f"\nAnswer preview (first 500 chars):")
        print("-" * 80)
        print(answer[:500])
        print("-" * 80)
        
        # Check for key elements
        print(f"\nKey elements check:")
        print(f"  Has 'Keywords:': {'Keywords:' in answer or 'keywords:' in answer.lower()}")
        print(f"  Has 'Quick Answer': {'Quick Answer' in answer or 'quick answer' in answer.lower()}")
        print(f"  Has 'Reflection': {'Reflection' in answer or 'reflection' in answer.lower()}")
        print(f"  Has 'Related Concepts': {'Related Concepts' in answer or 'related concepts' in answer.lower()}")
        print(f"  Has character name: {any(name in answer for name in ['Priya', 'Maya', 'Alex', 'Sam'])}")
        
        print("\n" + "="*80)
        print("TEST COMPLETE")
        print("="*80 + "\n")


if __name__ == "__main__":
    asyncio.run(test_pipeline())

