import streamlit as st

st.title("📊 Dashboard")

# Simulating login state
if st.session_state.get("logged_in", False):
    # Replace with actual dynamic values
    career_matches = 3  # This could be fetched from a database
    quizzes_taken = 1  # This could be a dynamic count
    feedback_submitted = "Yes"  # This could be fetched from user feedback data
    
    st.write("Welcome to your personalized dashboard!")
    st.metric("Career Matches", career_matches)
    st.metric("Quizzes Taken", quizzes_taken)
    st.metric("Feedback Submitted", feedback_submitted)
else:
    st.warning("Please login first from the Login page.")