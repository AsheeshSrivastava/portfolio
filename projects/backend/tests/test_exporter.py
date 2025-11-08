from app.schemas.chat import Citation, EvaluationSummary
from app.services.exporter import render_markdown, render_json, render_pdf


def sample_citations():
    return [
        Citation(id="doc-1", source="Document A", type="document"),
        Citation(id="web-1", source="https://example.com", type="web"),
    ]


def sample_evaluation():
    return EvaluationSummary(
        total_score=92.5,
        passed=True,
        coverage_score=0.8,
        citation_density=1.2,
        exec_ok=True,
        scope_ok=True,
        feedback=["Well done"],
        criteria={},
    )


def test_render_markdown():
    markdown = render_markdown("Answer", sample_citations(), sample_evaluation())
    assert "# Research Portal Response" in markdown
    assert "Document A" in markdown


def test_render_json():
    payload = render_json("Answer", sample_citations(), sample_evaluation())
    assert b"\"answer\": \"Answer\"" in payload


def test_render_pdf():
    pdf_bytes = render_pdf("Answer", sample_citations(), sample_evaluation())
    assert pdf_bytes.startswith(b"%PDF")




