def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns one of: "Win", "Too High", "Too Low".

    A guess ABOVE the secret is "Too High"; a guess BELOW it is "Too Low".
    Falls back to a string comparison when guess and secret are different
    types (e.g. an int guess against a stringified secret).
    """
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        return "Too Low"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def attempts_remaining(attempt_limit: int, attempts_used: int) -> int:
    """Return how many attempts are left in the game.

    `attempts_used` is 0 for a brand-new game and increases by exactly 1 for
    each submitted guess, so the first guess must reduce the result by 1.
    """
    return attempt_limit - attempts_used
