import streamlit as st

st.title("📝 Career Quiz")

# Use selectbox to allow an empty selection
q1 = st.selectbox("Do you enjoy solving problems?", ["", "Yes", "No"], index=0)
q2 = st.selectbox("Do you like working with computers?", ["", "Yes", "No"], index=0)
q3 = st.selectbox("Are you interested in helping others?", ["", "Yes", "No"], index=0)

if st.button("Get Career Suggestion"):
    # Check if all questions are answered (none are empty)
    if q1 and q2 and q3:
        score = sum([q == "Yes" for q in [q1, q2, q3]])
        if score == 3:
            st.success("You might enjoy a career in Software Engineering or Data Science!")
        elif score == 2:
            st.success("You may consider Business Analyst or Teaching roles.")
        else:
            st.info("Try exploring different paths in our Career Explorer section.")
    else:
        st.warning("Please answer all questions before getting a suggestion.")