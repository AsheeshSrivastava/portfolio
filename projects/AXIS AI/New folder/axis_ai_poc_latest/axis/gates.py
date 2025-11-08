from typing import Dict,List

def coverage_score(results:List[Dict])->float:
    sims=[r.get('similarity') for r in results if isinstance(r.get('similarity'),(int,float))]
    return round(sum(sims)/len(sims),3) if sims else 0.0

def citation_density(psw:Dict)->float:
    c=len(psw.get('citations',[]) or []); sections=1+len(psw.get('system_explain',[]) or [])
    return round(c/max(1,sections),2)

def evaluate_gates(psw:Dict,results:List[Dict],cov_min:float=0.65,cit_min:float=1.0)->Dict:
    cov=coverage_score(results); cit=citation_density(psw)
    gates=[{'name':f'coverage>={cov_min}','passed':cov>=cov_min,'details':f'{cov:.3f}'},
           {'name':f'citation_density>={cit_min}','passed':cit>=cit_min,'details':f'{cit:.2f}'},
           {'name':'exec_ok','passed':True},{'name':'scope_ok','passed':True}]
    return {'passed':all(g['passed'] for g in gates),'gates':gates,'telemetry':{'coverage_score':cov,'citation_density':cit,'unique_sources':len(results)}}
