def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def new_game_state(secret: int):
    """
    Return the fresh game state for a new game as a dict.

    Pure game logic: resets ALL game fields (attempts, secret, score,
    status, history). The caller passes in the chosen secret so this stays
    free of UI/randomness concerns.
    """
    return {
        "attempts": 0,
        "secret": secret,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX (agent mode): Compare as ints only — removed the TypeError fallback
    # that did lexicographic string compare, and corrected the hint direction
    # ("Too High" -> go LOWER). AI diagnosed the bug, I confirmed the fix.
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
