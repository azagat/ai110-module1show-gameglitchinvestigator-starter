from logic_utils import attempts_remaining, check_guess

# The live game logic lives in app.py; import its check_guess for hint-message
# regression tests. Aliased to avoid clashing with the logic_utils import above.
from app import check_guess as app_check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_fresh_game_starts_with_full_attempts():
    # A brand-new game has used 0 attempts, so all attempts are available.
    # (Regression: the counter used to start at 1, showing limit - 1.)
    assert attempts_remaining(8, 0) == 8


def test_first_guess_is_counted():
    # Regression test for the attempt-counter bug: the very first submitted
    # guess must reduce "attempts left" by exactly 1. Previously the counter
    # was displayed before being incremented, so the first guess looked free.
    limit = 8
    attempts_used = 0          # fresh game
    attempts_used += 1         # player submits their first guess
    assert attempts_remaining(limit, attempts_used) == limit - 1
    assert attempts_remaining(limit, attempts_used) == 7


# --- Regression tests for the swapped hint-message bug (app.py) -------------
# A guess ABOVE the secret is "Too High", so the hint must tell the player to
# go LOWER. A guess BELOW the secret must tell them to go HIGHER. The messages
# were previously reversed.

def test_too_high_hint_says_go_lower():
    outcome, message = app_check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_hint_says_go_higher():
    outcome, message = app_check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_returns_win():
    outcome, message = app_check_guess(50, 50)
    assert outcome == "Win"


def test_hints_against_string_secret_are_not_swapped():
    # On even attempts the app compares against a stringified secret, hitting
    # the TypeError fallback. The same hint direction must hold there.
    outcome, message = app_check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = app_check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
