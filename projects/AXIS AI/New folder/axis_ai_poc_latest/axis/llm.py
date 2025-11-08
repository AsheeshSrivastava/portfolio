import json,re,os
from typing import List,Dict
from openai import OpenAI
_ALLOWED_MODES={'coach','hybrid','socratic'}

def _mode_note(mode:str)->str:
    return {'coach':'Explain briefly, show a tiny example, then 1 mini task. Be encouraging and concrete.','hybrid':'Mix: short explanation + 2 guiding questions + 1 hint. Offer a tiny task.','socratic':'Socratic: ask up to 3 tiered questions before revealing code. Reveal a short solution only if stuck.'}.get(mode,'coach')

def _build_messages(query:str,retrieved:List[Dict],mode:str)->list:
    ctx='\n'.join([f"[{r['rank']}] {r['title']}: {r['snippet']}" for r in retrieved])
    system=("You are AXIS AI for a Python course. Domain scope: core Python, NumPy, pandas, Matplotlib, seaborn, scikit-learn. Use only the provided context to answer.\n"
            "Return STRICT JSON only with this schema:\n{\n  \"problem_restate\": str,\n  \"system_explain\": [str, ...],\n  \"win_steps\": [{\"action\": str}, ...],\n  \"mode_guidance\": {\"type\": \"coach|hybrid|socratic\"},\n  \"citations\": [{\"source\": \"vector\", \"title\": str, \"locator\": \"rank:N\"}],\n  \"next_action\": str\n}\n"
            "Rules: keep answers short, every claim supported by retrieved context; include at least 1 citation.")
    user=f"User question: {query}\n\nRetrieved context (ranked):\n{ctx}\n\nPedagogy mode: {mode}. Guidance: {_mode_note(mode)}\nRespond with JSON only."
    return [{'role':'system','content':system},{'role':'user','content':user}]

def _parse_json(text:str)->Dict:
    try:
        return json.loads(text)
    except Exception:
        m=re.search(r"\{.*\}",text,re.DOTALL)
        if m:
            try: return json.loads(m.group(0))
            except Exception: pass
    return {'problem_restate':'Could not parse model JSON.','system_explain':['Try again with a simpler question.'],'win_steps':[{'action':'Re-run with a shorter prompt'}],'mode_guidance':{'type':'coach'},'citations':[],'next_action':'Ask a focused question (one topic).'}

def answer_psw(query:str,retrieved:List[Dict],mode:str='coach',model:str|None=None)->Dict:
    mode=(mode or 'coach').lower().strip()
    if mode not in _ALLOWED_MODES: mode='coach'
    client=OpenAI(); model=model or os.getenv('OPENAI_MODEL_NAME','gpt-4o-mini')
    resp=client.chat.completions.create(model=model,messages=_build_messages(query,retrieved,mode),temperature=0.2,max_tokens=500)
    return _parse_json(resp.choices[0].message.content)
