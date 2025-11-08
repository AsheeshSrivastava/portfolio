# AXIS AI — Step 1: Health Check

## Run locally
pip install fastapi uvicorn
uvicorn axis.server:app --reload

## Test
Open http://127.0.0.1:8000/health
# -> {"status":"ok"}