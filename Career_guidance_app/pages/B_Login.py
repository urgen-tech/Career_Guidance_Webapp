import streamlit as st
import json
import os

USER_DATA_FILE = "users.json"

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Helper Functions
def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Main App
st.title("🔐 Login / Signup")

option = st.radio("Choose an option", ("Login", "Signup"))

users = load_users()

if option == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

elif option == "Signup":
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if new_username in users:
            st.error("Username already exists.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            users[new_username] = new_password
            save_users(users)
            st.success("Signup successful! You can now log in.")

# Post-login message
if st.session_state.logged_in:
    st.info(f"Welcome, {username}! You are logged in.")