import random
import streamlit as st

st.set_page_config(page_title="Guess the Number", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("I have selected a secret number between 1 and 100. Can you guess it?")

# Create game values only when a new session starts
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = ""

def restart_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = ""

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    value=50,
    step=1,
    disabled=st.session_state.finished
)

if st.button("Check Guess", disabled=st.session_state.finished):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.session_state.message = "📉 Too low! Try a bigger number."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "📈 Too high! Try a smaller number."
    else:
        st.session_state.message = (
            f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts."
        )
        st.session_state.finished = True

if st.session_state.message:
    if st.session_state.finished:
        st.success(st.session_state.message)
        st.balloons()
    else:
        st.info(st.session_state.message)

st.write(f"**Attempts:** {st.session_state.attempts}")

st.button("🔄 Restart Game", on_click=restart_game)
