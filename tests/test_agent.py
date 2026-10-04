from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'investigate the 5xx spike', "payload": {'facts': ['rollout of api-2.0 at 18:01']}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["rca"] == "bad_deploy"
    refused = client.post("/agent/run", json={"goal": 'page everyone and reboot fleet'}).json()
    assert refused["refused"] is True
