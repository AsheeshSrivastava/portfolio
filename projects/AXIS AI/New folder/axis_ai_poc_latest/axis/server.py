import time
from os import getenv
from fastapi import FastAPI,Query,HTTPException,Form
from fastapi.responses import RedirectResponse,Response,HTMLResponse
from axis.rag import ensure_seed,ask
from axis.llm import answer_psw
from axis.config import load_config,save_config
from axis.gates import evaluate_gates
app=FastAPI(title='AXIS AI',version='0.1.0')
@app.on_event('startup')
def _startup(): ensure_seed(); load_config()
@app.get('/')
def root(): return RedirectResponse(url='/docs',status_code=302)
@app.get('/favicon.ico',include_in_schema=False)
def favicon(): return Response(status_code=204)
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/ask')
def ask_endpoint(q: str = Query(..., min_length=3)):
    start=time.perf_counter(); results=ask(q,k=3); latency_ms=int((time.perf_counter()-start)*1000)
    return {'query':q,'results':results,'telemetry':{'latency_ms':latency_ms}}
@app.get('/answer')
def answer_endpoint(q: str = Query(..., min_length=3), mode: str = Query('coach', pattern='^(coach|hybrid|socratic)$')):
    try:
        t0=time.perf_counter(); retrieved=ask(q,k=2); model=getenv('OPENAI_MODEL_NAME','gpt-4o-mini'); psw=answer_psw(q,retrieved,mode=mode,model=model); gate_eval=evaluate_gates(psw,retrieved); latency_ms=int((time.perf_counter()-t0)*1000)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f'LLM error: {e}')
    return {'query':q,'mode':mode,'context':retrieved,'psw':psw,'gates':gate_eval['gates'],'passed':gate_eval['passed'],'telemetry':{**gate_eval['telemetry'],'model':model,'latency_ms':latency_ms}}
@app.get('/config',response_class=HTMLResponse)
def get_config():
    cfg=load_config(); masked=('********'+cfg['OPENAI_API_KEY'][-4:]) if cfg['OPENAI_API_KEY'] else ''
    return f"""
    <html><body style='font-family:system-ui;margin:2rem;max-width:720px;'>
      <h2>AXIS Config</h2>
      <form method='post' action='/config'>
        <label>OpenAI API Key</label><br/>
        <input type='password' name='openai_api_key' value='' placeholder='{masked}' style='width:100%;padding:.5rem'/><br/><br/>
        <label>Model</label><br/>
        <input name='openai_model_name' value='{cfg['OPENAI_MODEL_NAME']}' style='width:100%;padding:.5rem'/><br/><br/>
        <button type='submit' style='padding:.5rem 1rem;'>Save</button>
      </form>
      <p style='color:#666;margin-top:1rem'>Saved to <code>.env.local</code> on your machine (never committed).</p>
      <p><a href='/docs'>Open API docs</a></p>
    </body></html>
    """
@app.post('/config',response_class=HTMLResponse)
def post_config(openai_api_key: str = Form(''), openai_model_name: str = Form('gpt-4o-mini')):
    save_config(openai_api_key.strip(), openai_model_name.strip())
    return """<html><body style='font-family:system-ui;margin:2rem;'>
      <p>✅ Saved. You can now <a href='/docs'>try /answer</a>.</p>
      <p><a href='/config'>Back</a></p>
    </body></html>"""
