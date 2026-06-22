from logic_utils import check_guess, new_game_state


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_high_guess_says_go_lower():
    # Regression: a guess above the secret must direct the player DOWN.
    outcome, message = check_guess(80, 9)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_low_guess_says_go_higher():
    # Regression: a guess below the secret must direct the player UP.
    outcome, message = check_guess(9, 80)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_exact_guess_wins():
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"


def test_lexicographic_trap_compares_numerically():
    # "80" < "9" as strings, but 80 > 9 as numbers. The old code converted
    # the secret to a string on even attempts, flipping the direction.
    outcome, message = check_guess(80, 9)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_new_game_resets_all_fields():
    # Regression: New Game previously reset only attempts/secret, leaving
    # status/score/history stale — which froze the board after a win/loss.
    state = new_game_state(secret=42)
    assert state == {
        "attempts": 0,
        "secret": 42,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def test_new_game_status_is_playing():
    # The key fix: status must be reset to "playing" so the game isn't
    # halted by the "already won / game over" guard on the next rerun.
    assert new_game_state(secret=7)["status"] == "playing"


def test_new_game_uses_provided_secret():
    # Secret comes from the caller (the chosen difficulty range), not hardcoded.
    assert new_game_state(secret=15)["secret"] == 15


def test_new_game_history_is_fresh_list():
    # History should be a new empty list, not shared across games.
    first = new_game_state(secret=1)
    first["history"].append(99)
    second = new_game_state(secret=1)
    assert second["history"] == []
