from typing import List, Dict
import chromadb
from chromadb.utils import embedding_functions
_client = chromadb.Client()
_embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')
_coll = _client.get_or_create_collection(name='aethelgard_py', embedding_function=_embedder, metadata={'hnsw:space':'cosine'})
_STARTER_DOCS=[{'id':'doc1','title':'Python — List Comprehensions','text':'List comprehensions create lists using [expr for item in iterable if cond]. They are concise and often faster than for-loops for simple transformations.'},{'id':'doc2','title':'NumPy — Vectorization & Broadcasting','text':'Vectorization uses NumPy arrays to apply operations across data without Python loops. Broadcasting automatically expands shapes when possible (e.g., (3,1) + (1,4) -> (3,4)).'}]

def ensure_seed()->None:
    if _coll.count()==0:
        _coll.add(ids=[d['id'] for d in _STARTER_DOCS],documents=[d['text'] for d in _STARTER_DOCS],metadatas=[{'title':d['title']} for d in _STARTER_DOCS])

def ask(query:str,k:int=3)->List[Dict]:
    res=_coll.query(query_texts=[query],n_results=k,include=['metadatas','documents','distances'])
    docs=res['documents'][0]; metas=res['metadatas'][0]; dists=res.get('distances',[[None]*len(docs)])[0]
    out=[]
    for i,(doc,meta,dist) in enumerate(zip(docs,metas,dists),start=1):
        snippet=doc[:220]+('...' if len(doc)>220 else '')
        similarity=None if dist is None else round(1-float(dist),3)
        out.append({'rank':i,'title':meta.get('title',''),'similarity':similarity,'snippet':snippet})
    return out
