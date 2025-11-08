
# axis/server.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import RedirectResponse, Response
from axis.rag import ensure_seed, ask
from axis.llm import answer_psw
from os import getenv

app = FastAPI(title="AXIS AI", version="0.0.3")

@app.on_event("startup")
def _startup():
    ensure_seed()

@app.get("/")
def root():
    return RedirectResponse(url="/docs", status_code=302)

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ask")
def ask_endpoint(q: str = Query(..., min_length=3)):
    return {"query": q, "results": ask(q, k=3)}

@app.get("/answer")
def answer_endpoint(
    q: str = Query(..., min_length=3),
    mode: str = Query("coach", pattern="^(coach|hybrid|socratic)$")
):
    try:
        retrieved = ask(q, k=2)
        model = getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")  # override via env if needed
        psw = answer_psw(q, retrieved, mode=mode, model=model)
        return {"query": q, "mode": mode, "context": retrieved, "psw": psw}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")
