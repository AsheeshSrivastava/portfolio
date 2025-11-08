from fastapi.testclient import TestClient
from axis.server import app

def test_ask_returns_results():
    client = TestClient(app)
    r = client.get('/ask', params={'q':'broadcasting in numpy'})
    assert r.status_code == 200
    data = r.json()
    assert 'results' in data and isinstance(data['results'], list)
    assert len(data['results']) >= 1
