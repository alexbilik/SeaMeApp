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

# Button for the target color.
# When pressed, we check if the current box color matches the target color.
if st.button(st.session_state.target_color):
    if st.session_state.current_color == st.session_state.target_color:
        st.session_state.score += 1
    else:
        st.session_state.score -= 1
    # Update target color for the next round
    st.session_state.target_color = random.choice(colors)
    # Optional: also update the box color immediately after the button press
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
    # Wait for the current timer value.
    time.sleep(st.session_state.timer)
    # Change the box color randomly.
    st.session_state.current_color = random.choice(colors)
    # Decrease the timer by 0.1 sec but keep a lower bound (for example, 0.1 sec)
    st.session_state.timer = max(0.1, st.session_state.timer - 0.1)
    # Rerun the script to update the UI.
    st.experimental_rerun()

# Footer text
st.markdown("---")
st.write("Game created by Noam Buslovich")
