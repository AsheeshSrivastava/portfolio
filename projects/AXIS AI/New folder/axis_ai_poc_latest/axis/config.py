import os
from pathlib import Path
from dotenv import load_dotenv,set_key
ENV_FILE=(Path(__file__).resolve().parent.parent/'.env.local')

def load_config()->dict:
    if ENV_FILE.exists(): load_dotenv(dotenv_path=ENV_FILE,override=False)
    return {'OPENAI_API_KEY':os.getenv('OPENAI_API_KEY',''),'OPENAI_MODEL_NAME':os.getenv('OPENAI_MODEL_NAME','gpt-4o-mini')}

def save_config(openai_key:str,model:str)->None:
    ENV_FILE.touch(exist_ok=True); set_key(str(ENV_FILE),'OPENAI_API_KEY',openai_key or ''); set_key(str(ENV_FILE),'OPENAI_MODEL_NAME',model or 'gpt-4o-mini')
    os.environ['OPENAI_API_KEY']=openai_key or ''
    os.environ['OPENAI_MODEL_NAME']=model or 'gpt-4o-mini'
