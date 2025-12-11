import streamlit as st

st.title("🔍 Career Explorer")

career = st.selectbox("Select a Career to Learn More", ["Software Engineer", "Doctor", "Teacher", "Entrepreneur"])

careers_info = {
    "Software Engineer": "Designs and builds software applications. Requires coding skills.",
    "Doctor": "Helps people maintain health. Requires medical school and certifications.",
    "Teacher": "Educates students. Can specialize in different age groups or subjects.",
    "Entrepreneur": "Starts businesses, identifies problems, and offers solutions."
}

st.write(careers_info[career])