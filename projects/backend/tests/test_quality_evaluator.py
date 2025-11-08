import base64
import os

import pytest

from app.quality.evaluator import QualityEvaluator
from app.quality.rubric import TOTAL_POINTS


def _sample_documents():
    return [
        {
            "document_id": "doc-1",
            "document_title": "Python Concurrency",
            "content": "Content",
            "score": 0.2,
            "chunk_index": 0,
        },
        {
            "document_id": "doc-2",
            "document_title": "Async IO",
            "content": "Content",
            "score": 0.3,
            "chunk_index": 1,
        },
    ]


def _sample_citations():
    return [
        {
            "id": "doc-1",
            "source": "Python Concurrency",
            "type": "document",
            "metadata": {"document_id": "doc-1", "chunk_index": 0},
        },
        {
            "id": "doc-2",
            "source": "Async IO",
            "type": "document",
            "metadata": {"document_id": "doc-2", "chunk_index": 1},
        },
    ]


def test_quality_evaluator_passes_high_quality_answer():
    evaluator = QualityEvaluator()
    documents = _sample_documents()
    citations = _sample_citations()
    answer = """\
```python
import asyncio

async def main():
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

1. Identify the problem context (I/O bound tasks).
2. Configure the event loop inside your system.
3. Win by reducing latency.

Consider iterating on this design with structured tasks so you can scaffold learning.
[doc-1] [doc-2]
"""

    report = evaluator.evaluate(
        question="How do I structure Python async programs?",
        answer=answer,
        documents=documents,
        citations=citations,
    )

    assert report.passed
    assert report.total_score <= TOTAL_POINTS
    assert report.coverage_score >= 0.65
    assert report.citation_density >= 1.0


def test_quality_evaluator_flags_low_quality_answer():
    evaluator = QualityEvaluator()
    report = evaluator.evaluate(
        question="Explain async in Python",
        answer="Async is cool. You should figure it out yourself. No citations.",
        documents=_sample_documents(),
        citations=[],
    )

    assert not report.passed
    assert report.coverage_score < 0.65
    assert report.feedback




