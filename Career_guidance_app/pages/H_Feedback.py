import streamlit as st

st.title("✉ Feedback")

name = st.text_input("Your Name")

# Number-based rating (like stars)
rating = st.radio("Rate this app (1 = worst, 5 = best)", [1, 2, 3, 4, 5], horizontal=True)

comments = st.text_area("Additional Feedback")

if st.button("Submit"):
    st.success("Thanks for your feedback!")
    st.write("Here’s what you submitted:")
    st.write(f"Name: {name}")
    st.write(f"Rating: {rating} out of 5")
    st.write(f"Comments: {comments}")