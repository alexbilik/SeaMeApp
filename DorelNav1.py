import streamlit as st

# Define riddle data: question, correct answer, and next location (Google Maps link or gathering point link)
riddles = {
    1: {
        "description": "You are at Point 1. Solve the riddle: What is 2 + 2?",
        "answer": "4",
        "next_link": "https://www.google.com/maps/place/Location+1"
    },
    2: {
        "description": "You are at Point 2. Solve the riddle: What is the capital of France?",
        "answer": "Paris",
        "next_link": "https://www.google.com/maps/place/Location+2"
    },
    3: {
        "description": "You are at Point 3. Solve the riddle: What color do you get when you mix blue and yellow?",
        "answer": "green",
        "next_link": "https://www.google.com/maps/place/Location+3"
    },
    4: {
        "description": "You are at Point 4. Solve the riddle: What is the square root of 16?",
        "answer": "4",
        "next_link": "https://www.google.com/maps/place/Location+4"
    },
    5: {
        "description": "You are at the final point. Solve the riddle: What is the chemical symbol for water?",
        "answer": "H2O",
        "gathering_link": "https://www.google.com/maps/place/Gathering+Point"
    }
}

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "main"
if "selected_riddle" not in st.session_state:
    st.session_state.selected_riddle = None
if "riddle_error" not in st.session_state:
    st.session_state.riddle_error = ""

def main_page():
    st.title("Navigation Game")
    st.write("Enter the riddle number to start (1 to 5):")

    riddle_num = st.text_input("Riddle Number", key="riddle_input")
    if st.button("Submit Riddle Number"):
        try:
            riddle_num = int(riddle_num)
            if riddle_num in riddles:
                st.session_state.selected_riddle = riddle_num
                st.session_state.page = "riddle"
                st.session_state.riddle_error = ""
                # st.stop()
            else:
                st.session_state.riddle_error = "Riddle number does not exist."
        except ValueError:
            st.session_state.riddle_error = "Please enter a valid number."

    if st.session_state.riddle_error:
        st.error(st.session_state.riddle_error)

def riddle_page():
    riddle_num = st.session_state.selected_riddle
    current_riddle = riddles[riddle_num]
    st.header(f"Riddle {riddle_num}")
    if st.button("Back to Main"):
        st.session_state.page = "main"
        # st.stop()

    st.write(current_riddle["description"])

    answer = st.text_input("Your Answer", key="riddle_answer")
    if st.button("Submit Answer"):
        if answer.strip().lower() == current_riddle["answer"].lower():
            if riddle_num < 5:
                st.success("Correct!")
                st.markdown(f"[Next Point]({current_riddle['next_link']})")
            else:
                # Last riddle so go to congrats page
                st.session_state.page = "congrats"
                # st.stop()
        else:
            st.error("Wrong answer. Please try again.")

def congrats_page():
    st.title("Congratulations!")
    st.success("You have solved all the riddles!")
    # Use the gathering link from riddle 5
    gather_link = riddles[5]["gathering_link"]
    st.markdown(f"[Go to Gathering Point]({gather_link})")
    if st.button("Back to Main"):
        # Reset state to allow replay
        st.session_state.page = "main"
        st.session_state.selected_riddle = None
        # st.stop()

# Page routing
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "riddle":
    riddle_page()
elif st.session_state.page == "congrats":
    congrats_page()