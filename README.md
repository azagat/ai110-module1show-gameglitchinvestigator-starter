# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
- [X] Detail which bugs you found.
- [X] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Enter 89
2. Game says "Go LOWER!" and one less attempt is left
3. Enter 50
4. Game says "Go HIGHER!" and one less attempt is left
5. Game continues until the correct number is guessed or there are no more attempts. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
tests/test_game_logic.py::test_winning_guess PASSED                                                                                                [ 11%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                               [ 22%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                [ 33%]
tests/test_game_logic.py::test_fresh_game_starts_with_full_attempts PASSED                                                                         [ 44%]
tests/test_game_logic.py::test_first_guess_is_counted PASSED                                                                                       [ 55%]
tests/test_game_logic.py::test_too_high_hint_says_go_lower PASSED                                                                                  [ 66%]
tests/test_game_logic.py::test_too_low_hint_says_go_higher PASSED                                                                                  [ 77%]
tests/test_game_logic.py::test_correct_guess_returns_win PASSED                                                                                    [ 88%]
tests/test_game_logic.py::test_hints_against_string_secret_are_not_swapped PASSED                                                                  [100%]

=================================================================== 9 passed in 0.86s ====================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
