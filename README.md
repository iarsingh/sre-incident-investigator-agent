# AI SRE Incident Investigator

Phase 6

Skills: alerts, logs, metrics, git, k8s, previous incidents, approval

Alert → SRE agent → logs/metrics/git/k8s → previous incidents → RCA. Remediation needs human language avoided (page/reboot refused).

```bash
pip install -r requirements.txt
pytest -q
```

Laptop proof. No hosted model. Cluster apply stays false until a human approves.
