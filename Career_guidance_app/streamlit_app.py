import streamlit as st

st.set_page_config(page_title="Career Guidance App", page_icon="🎓", layout="wide")

st.markdown("""
    <h1 style='text-align: center;'>Welcome to the Career Guidance System</h1>
    <p style='text-align: center;'>Navigate using the sidebar to explore different features.</p>
""", unsafe_allow_html=True)

st.sidebar.success("Choose a section from the sidebar to get started.")