import streamlit as st
import streamlit.components.v1 as components

# Define your riddles here. Each riddle has a description, the correct answer, and a Google Maps link for the next point.
riddles = {
    1: {
        "description": "**Location 1:** Solve this riddle to find the first clue...",
        "answer": "5",
        "link": "https://www.google.com/maps?q=31.7767,35.2345"
    },
    2: {
        "description": "**Location 2:** A second challenge awaits you...",
        "answer": "5",
        "link": "https://www.google.com/maps?q=31.7780,35.2300"
    },
    3: {
        "description": "**Location 3:** The third puzzle is hidden near...",
        "answer": "5",
        "link": "https://www.google.com/maps?q=31.7795,35.2220"
    },
    4: {
        "description": "**Location 4:** Almost there—figure this out to proceed...",
        "answer": "5",
        "link": "https://www.google.com/maps?q=31.7810,35.2150"
    },
    5: {
        "description": "**Location 5:** Final riddle before the gathering point...",
        "answer": "5",
        "link": None  # No next link, this is the last one
    }
}

# Link for the final gathering point
gathering_link = "https://www.google.com/maps?q=31.7830,35.2100"

# Helper to reset to main screen
def go_home():
    st.session_state['stage'] = 'select'


def main():
    # Initialize session state
    if 'stage' not in st.session_state:
        st.session_state['stage'] = 'select'
    if 'last_location' not in st.session_state:
        st.session_state['last_location'] = None

    # Riddle selection screen
    if st.session_state['stage'] == 'select':
        st.title("🔍 Enter Riddle Number")

        # Show last found location if available
        if st.session_state['last_location']:
            st.markdown("---")
            st.subheader("🏁 Next Point to Navigate:")
            st.markdown(f"[Open in Google Maps]({st.session_state['last_location']})")
            components.iframe(st.session_state['last_location'], height=300, scrolling=False)
            st.info("Go to the next location and look for the envelop containing the next riddle")
            st.markdown("---")

        r_num = st.number_input(
            "Riddle Number", min_value=1, max_value=len(riddles), step=1, value=1, key='riddle_input'
        )
        if st.button("Go"):
            if r_num in riddles:
                st.session_state['current_riddle'] = r_num
                st.session_state['stage'] = 'answer'
                st.rerun()
            else:
                st.error("Riddle number does not exist. Please try again.")

    # Riddle answer screen
    elif st.session_state['stage'] == 'answer':
        rid = st.session_state['current_riddle']
        solved_key = f"solved_{rid}"
        if solved_key not in st.session_state:
            st.session_state[solved_key] = False

        st.header(f"Riddle {rid}")
        if st.button("🏠 Home"):
            go_home()
            st.rerun()

        # Show the riddle description
        st.write(riddles[rid]['description'])

        # If already solved: make read-only and show next link
        if st.session_state[solved_key]:
            next_link = riddles[rid]['link'] or gathering_link
            st.success("✅ Correct!")
            st.markdown(f"**Next Point:** [Open in Google Maps]({next_link})")
            st.markdown(f"{next_link}")
            components.iframe(next_link, height=300, scrolling=False)
            st.info("Go to the next location and look for the envelop containing the next riddle")

        else:
            # User answer input
            user_ans = st.text_input("Your Answer", key='answer_input')
            if st.button("Submit"):
                correct = riddles[rid]['answer'].strip().lower()
                if user_ans.strip().lower() == correct:
                    # Mark solved and update last location
                    st.session_state[solved_key] = True
                    next_link = riddles[rid]['link'] or gathering_link
                    st.session_state['last_location'] = next_link
                    # Show results immediately
                    if rid == len(riddles):
                        st.balloons()
                        st.success("🎉 Congratulations! You've completed the game.")
                        st.markdown(f"**Gathering Point:** [Open in Google Maps]({gathering_link})")
                        components.iframe(next_link, height=300, scrolling=False)
                    else:
                        st.success("✅ Correct!")
                        st.markdown(f"**Next Point:** [Open in Google Maps]({next_link})")
                        components.iframe(next_link, height=300, scrolling=False)
                        st.info("Go to the next location and look for the envelop containing the next riddle")
                else:
                    st.error("❌ Wrong answer. Please try again.")


if __name__ == "__main__":
    main()
