from logic_utils import check_guess

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

# Bug: "You can't win" / "changing secret" — secret coerced to string on even attempts
# String comparison is lexicographic: "9" > "50" is True, so hints were wrong
# e.g. guessing 9 when secret is 50 would say "Too High / Go HIGHER" — impossible to converge
def test_string_secret_causes_wrong_hint():
    # With an int secret, 9 < 50 should say "Too Low"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"
    # With a string secret (the bug), "9" > "50" lexicographically → wrong outcome
    outcome_bugged, _ = check_guess(9, "50")
    assert outcome_bugged == "Too High", "reproduces the string-secret lexicographic bug"

# Bug: "The hints lie" — reversed Higher/Lower feedback
def test_hint_says_lower_when_guess_is_too_high():
    # Guessing 99 when secret is 1 — hint must say go lower, not higher
    _, message = check_guess(99, 1)
    assert "LOWER" in message.upper()

def test_hint_says_higher_when_guess_is_too_low():
    # Guessing 1 when secret is 99 — hint must say go higher, not lower
    _, message = check_guess(1, 99)
    assert "HIGHER" in message.upper()
