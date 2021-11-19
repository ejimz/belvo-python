from unittest.mock import MagicMock

from belvo import resources
from belvo.resources import risk_insights


def test_risk_insights_sends_token_if_given(api_session):
    risk_insights = resources.RiskInsights(api_session)
    risk_insights.session.post = MagicMock()
    risk_insights.create("fake-link-uuid", token="fake-token")

    risk_insights.session.post.assert_called_with(
        "/api/risk-insights/",
        data={"link": "fake-link-uuid", "save_data": True, "token": "fake-token"},
        raise_exception=False,
    )


def test_risk_insights_resume(api_session):
    risk_insights = resources.RiskInsights(api_session)
    risk_insights.session.patch = MagicMock()
    risk_insights.resume("fake-session", "fake-token")

    risk_insights.session.patch.assert_called_with(
        "/api/risk-insights/",
        data={"session": "fake-session", "token": "fake-token"},
        raise_exception=False,
    )
