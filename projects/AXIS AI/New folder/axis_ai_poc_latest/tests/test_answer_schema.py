from fastapi.testclient import TestClient
import axis.server as server

def fake_answer_psw(query, retrieved, mode='coach', model=None):
    return {'problem_restate':'You want list comprehensions.','system_explain':['They use [expr for item in iterable if cond].'],'win_steps':[{'action':'Write a one-line list comprehension'}],'mode_guidance':{'type':mode},'citations':[{'source':'vector','title':retrieved[0]['title'],'locator':'rank:1'}],'next_action':'Try transforming numbers 1..5 into squares.'}

def test_answer_psw_schema(monkeypatch):
    monkeypatch.setattr(server, 'answer_psw', fake_answer_psw)
    client = TestClient(server.app)
    r = client.get('/answer', params={'q':'Explain list comprehensions','mode':'coach'})
    assert r.status_code == 200
    data = r.json()
    assert 'psw' in data and 'citations' in data['psw']
    assert data['psw']['mode_guidance']['type'] == 'coach'
    assert 'gates' in data and isinstance(data['gates'], list)
    assert 'telemetry' in data
