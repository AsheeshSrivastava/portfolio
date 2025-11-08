"""Test if all imports work correctly."""

import sys
import io
import traceback

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_import(module_name: str, description: str) -> bool:
    """Test if a module can be imported."""
    try:
        __import__(module_name)
        print(f"[OK] {description}")
        return True
    except Exception as e:
        print(f"[FAIL] {description}")
        print(f"  Error: {e}")
        traceback.print_exc()
        return False

print("\n" + "="*60)
print("TESTING IMPORTS")
print("="*60 + "\n")

# Test basic imports
test_import("app.core.config", "Core config")
test_import("app.core.logging", "Core logging")
test_import("app.graph.types", "Graph types")

# Test multi-agent components
test_import("app.graph.complexity_classifier", "Complexity Classifier")
test_import("app.graph.scenario_architect", "Scenario Architect")
test_import("app.graph.cot_storyteller", "CoT Storyteller")
test_import("app.quality.narrative_evaluator", "Narrative Evaluator")
test_import("app.quality.aethelgard_evaluator", "Aethelgard Evaluator")
test_import("app.graph.narrative_enricher", "Narrative Enricher")

# Test main graph
test_import("app.graph.research_graph", "Research Graph")

print("\n" + "="*60)
print("Now testing instantiation...")
print("="*60 + "\n")

try:
    from app.graph.complexity_classifier import ComplexityClassifier
    classifier = ComplexityClassifier()
    print("[OK] ComplexityClassifier instantiated")
except Exception as e:
    print(f"[FAIL] ComplexityClassifier instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

try:
    from app.graph.scenario_architect import ScenarioArchitect
    architect = ScenarioArchitect()
    print("[OK] ScenarioArchitect instantiated")
except Exception as e:
    print(f"[FAIL] ScenarioArchitect instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

try:
    from app.graph.cot_storyteller import CoTStoryteller
    storyteller = CoTStoryteller()
    print("[OK] CoTStoryteller instantiated")
except Exception as e:
    print(f"[FAIL] CoTStoryteller instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

try:
    from app.quality.narrative_evaluator import NarrativeQualityEvaluator
    evaluator = NarrativeQualityEvaluator()
    print("[OK] NarrativeQualityEvaluator instantiated")
except Exception as e:
    print(f"[FAIL] NarrativeQualityEvaluator instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

try:
    from app.quality.aethelgard_evaluator import AethelgardQualityEvaluator
    evaluator = AethelgardQualityEvaluator()
    print("[OK] AethelgardQualityEvaluator instantiated")
except Exception as e:
    print(f"[FAIL] AethelgardQualityEvaluator instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

try:
    from app.graph.narrative_enricher import NarrativeEnricher
    enricher = NarrativeEnricher()
    print("[OK] NarrativeEnricher instantiated")
except Exception as e:
    print(f"[FAIL] NarrativeEnricher instantiation failed")
    print(f"  Error: {e}")
    traceback.print_exc()

print("\n" + "="*60)
print("IMPORT TEST COMPLETE")
print("="*60 + "\n")

