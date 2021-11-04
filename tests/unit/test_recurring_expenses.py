from unittest.mock import MagicMock

from belvo import resources


def test_recurring_expenses_sends_token_if_given(api_session):
    recurring_expenses = resources.RecurringExpenses(api_session)
    recurring_expenses.session.post = MagicMock()
    recurring_expenses.create("fake-link-uuid", token="fake-token")

    recurring_expenses.session.post.assert_called_with(
        "/api/recurring-expenses/",
        data={"link": "fake-link-uuid", "save_data": True, "token": "fake-token"},
        raise_exception=False,
    )


def test_recurring_expenses_resume(api_session):
    recurring_expenses = resources.RecurringExpenses(api_session)
    recurring_expenses.session.patch = MagicMock()
    recurring_expenses.resume("fake-session", "fake-token")

    recurring_expenses.session.patch.assert_called_with(
        "/api/recurring-expenses/",
        data={"session": "fake-session", "token": "fake-token"},
        raise_exception=False,
    )
