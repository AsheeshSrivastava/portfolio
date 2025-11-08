# axis/llm.py
import json, re
from typing import List, Dict
from openai import OpenAI

_ALLOWED_MODES = {"coach", "hybrid", "socratic"}

def _mode_note(mode: str) -> str:
    if mode == "coach":
        return ("Explain briefly, then show a tiny example, then 1 mini task. "
                "Be encouraging and concrete.")
    if mode == "hybrid":
        return ("Mix: short explanation (≈2 lines) + 2 guiding questions + 1 hint. "
                "Give a tiny task.")
    return ("Socratic: ask up to 3 tiered questions before revealing code. "
            "If user is stuck, reveal a short solution.")

def _build_messages(query: str, retrieved: List[Dict], mode: str) -> list:
    ctx_lines = []
    for i, r in enumerate(retrieved, start=1):
        ctx_lines.append(f"[{i}] {r['title']}: {r['snippet']}")
    context = "\n".join(ctx_lines)

    system = (
        "You are AXIS AI for a Python course. Domain scope: core Python, NumPy, pandas, "
        "Matplotlib, seaborn, scikit-learn. Use only the provided context to answer.\n"
        "Return STRICT JSON only with this schema:\n"
        "{\n"
        '  "problem_restate": str,\n'
        '  "system_explain": [str, ...],\n'
        '  "win_steps": [{"action": str}, ...],\n'
        '  "mode_guidance": {"type": "coach|hybrid|socratic"},\n'
        '  "citations": [{"source": "vector", "title": str, "locator": "rank:N"}],\n'
        '  "next_action": str\n'
        "}\n"
        "Rules: keep answers short and concrete; every claim should be supported by the retrieved context; "
        "include at least 1 citation."
    )

    user = (
        f"User question: {query}\n\n"
        f"Retrieved context (ranked):\n{context}\n\n"
        f"Pedagogy mode: {mode}. Guidance: {_mode_note(mode)}\n"
        "Respond with JSON only."
    )
    return [{"role": "system", "content": system},
            {"role": "user", "content": user}]

def _parse_json(text: str) -> Dict:
    # Try strict JSON first
    try:
        return json.loads(text)
    except Exception:
        # Fallback: extract the largest {...} block and parse
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
    # Very small safe fallback
    return {
        "problem_restate": "Could not parse model JSON.",
        "system_explain": ["Try again with a simpler question."],
        "win_steps": [{"action": "Re-run with a shorter prompt"}],
        "mode_guidance": {"type": "coach"},
        "citations": [],
        "next_action": "Ask a focused question (one topic)."
    }

def answer_psw(query: str, retrieved: List[Dict], mode: str = "coach",
               model: str = "gpt-4o-mini") -> Dict:
    mode = mode.lower().strip()
    if mode not in _ALLOWED_MODES:
        mode = "coach"
    client = OpenAI()  # uses OPENAI_API_KEY env var
    messages = _build_messages(query, retrieved, mode)
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=500,
    )
    text = resp.choices[0].message.content
    return _parse_json(text)
