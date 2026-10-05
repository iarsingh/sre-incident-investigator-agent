from agentx.progression import sre_rca

def test_sre_rca_holds_page():
    out = sre_rca("page the oncall", ["deploy abc"], {"err": 12}, ["deploy abc"], ["pod restart"], approved=False)
    assert out["needs_approval"] is True
    assert out["applied"] is False

