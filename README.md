# 🎯 Number Guessing Game

A beginner-friendly number guessing game built with Python and Streamlit.

The computer chooses a random number between **1 and 100**. The player enters guesses and receives hints telling them whether the secret number is higher or lower.

## Project files

```text
guess_game_full_project/
├── guess_game.ipynb
├── guess_game.py
├── app.py
├── requirements.txt
└── README.md
```

- **guess_game.ipynb** — Jupyter Notebook version of the Python game.
- **guess_game.py** — Python terminal/command-line version.
- **app.py** — Streamlit web application.
- **requirements.txt** — Python package dependencies.
- **README.md** — Project documentation and instructions.

## Requirements

- Python 3.8 or newer
- Jupyter Notebook or JupyterLab (for the notebook)
- Streamlit (for the web app)

## Run the Python version

Open a terminal in this folder and run:

```bash
python guess_game.py
```

## Open the Jupyter Notebook

Start Jupyter:

```bash
pip install notebook
jupyter notebook
```

Then open `guess_game.ipynb` and run its cells from top to bottom.

## Run the Streamlit app locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Streamlit will open the app in your browser.

## Deploy on Streamlit Community Cloud

1. Upload all five project files to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in and connect your GitHub account.
4. Choose the repository and branch.
5. Set the **Main file path** to `app.py`.
6. Deploy the app.

Keep `requirements.txt` in the root of the repository so Streamlit can install the dependency.

## Python concepts used

- `random.randint()` — generates the secret number.
- `input()` — takes input from the player.
- `int()` — converts input into an integer.
- `while` loop — repeats the game until the player wins.
- `if`, `elif`, and `else` — compare the guess with the secret number.
- `try` and `except` — handle invalid input.
- `st.session_state` — preserves game data between Streamlit reruns.

## Possible improvements

- Add Easy, Medium, and Hard difficulty levels.
- Limit the number of attempts.
- Add a score and best-score system.
- Add a timer.
