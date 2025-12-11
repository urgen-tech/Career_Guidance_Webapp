import streamlit as st

st.title("📄 Resume Builder")

name = st.text_input("Your Full Name")
email = st.text_input("Email Address")
skills = st.text_area("List Your Skills (comma separated)")
projects = st.text_area("Describe Your Projects")

if st.button("Generate Resume"):
    st.markdown(f"""
    *Name:* {name}  
    *Email:* {email}  
    *Skills:* {skills}  
    *Projects:*  
    {projects}
    """)
    st.success("Copy the resume above or use a template to export it.")