TOOLS = ["logs", "metrics", "git", "kubernetes", "prior_incidents", "runbooks", "rca"]
WRITES = ("page everyone", "reboot fleet", "kubectl apply",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    facts = " ".join(payload.get("facts") or []).lower(); result = "bad_deploy" if "rollout" in facts else "saturation" if "cpu" in facts else "unknown"
    return {"refused": False, "tools": TOOLS, "rca": result, "applied": False, "needs_approval": False}
