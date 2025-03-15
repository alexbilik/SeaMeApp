import streamlit as st
import time, random

# Define the list of 10 colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]

# Initialize session state variables if they don't exist yet.
if "score" not in st.session_state:
    st.session_state.score = 0
if "timer" not in st.session_state:
    st.session_state.timer = 1.5  # starting interval in seconds
if "current_color" not in st.session_state:
    st.session_state.current_color = random.choice(colors)
if "target_color" not in st.session_state:
    st.session_state.target_color = random.choice(colors)
if "game_running" not in st.session_state:
    st.session_state.game_running = False
if "message" not in st.session_state:
    st.session_state.message = ""

st.title("Color Match Game")
st.write("Press the button when the color of the box matches the color written on the button.")

# Display the color box at the center using HTML/CSS
box_html = f"""
<div style="width:200px; height:200px; margin:auto; border: 2px solid black; background-color:{st.session_state.current_color};">
</div>
"""
st.markdown(box_html, unsafe_allow_html=True)

# Display the current score
st.subheader(f"Score: {st.session_state.score}")

# Display the current timer value
st.subheader(f"Timer: {st.session_state.timer:.1f} seconds")

# Display success or failure message
if st.session_state.message:
    st.markdown(f"<div style='color: {st.session_state.message_color}; font-size: 24px; text-align: center;'>{st.session_state.message}</div>", unsafe_allow_html=True)
    time.sleep(1)
    st.session_state.message = ""

# Button for the target color.
if st.button(st.session_state.target_color):
    st.session_state.timer = max(0.1, st.session_state.timer - 0.1)
    if st.session_state.current_color == st.session_state.target_color:
        st.session_state.score += 1
        st.session_state.message = "SUCCESS"
        st.session_state.message_color = "green"
    else:
        st.session_state.score -= 1
        st.session_state.message = "Fail..."
        st.session_state.message_color = "red"
    # Update target color for the next round
    st.session_state.target_color = random.choice(colors)
    # Optional: update the box color immediately after the button press
    st.session_state.current_color = random.choice(colors)

# Start game button: set the game_running flag to True.
if st.button("Start Game"):
    st.session_state.game_running = True

# Reset game button: resets all variables.
if st.button("Reset Game"):
    st.session_state.score = 0
    st.session_state.timer = 1.5
    st.session_state.current_color = random.choice(colors)
    st.session_state.target_color = random.choice(colors)
    st.session_state.game_running = False

# If the game is running, update the color automatically every X seconds.
if st.session_state.game_running:
    if st.session_state.timer <= 0.1:
        st.session_state.message = f"Game Over! Your score: {st.session_state.score}"
        st.session_state.message_color = "blue"
        st.session_state.game_running = False
        st.session_state.timer = 1.5
        st.session_state.score = 0
    else:
        time.sleep(st.session_state.timer)
        st.session_state.current_color = random.choice(colors)
        st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

# Footer text
st.markdown("---")
st.write("Game created by Noam Buslovich")
