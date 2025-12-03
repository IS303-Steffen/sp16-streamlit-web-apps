'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Build a mini dashboard that:
- Takes user input for name (text), age (number), and favorite animal (selectbox)
- Uses a form to submit all at once
- Stores the submitted data in st.session_state so it doesn't disappear after re-runs
- Displays a summary below the form like:

    "Name: Alex | Age: 23 | Favorite Animal: Dolphin"

Also include a "Clear" button to wipe all saved values.
'''

import streamlit as st

if "submitted" not in st.session_state:
    st.session_state.submitted = False
    st.session_state.name = ""
    st.session_state.age = 0
    st.session_state.animal = ""

with st.form("dashboard_form"):
    name = st.text_input("Name:", value=st.session_state.name)
    age = st.number_input("Age:", min_value=0, step=1, value=st.session_state.age)
    animal = st.selectbox("Favorite Animal:", ["Cat", "Dog", "Dolphin", "Penguin"], index=0)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.name = name
        st.session_state.age = age
        st.session_state.animal = animal
        st.session_state.submitted = True

if st.session_state.submitted:
    st.write(f"Name: {st.session_state.name} | Age: {st.session_state.age} | Favorite Animal: {st.session_state.animal}")

if st.button("Clear"):
    st.session_state.name = ""
    st.session_state.age = 0
    st.session_state.animal = ""
    st.session_state.submitted = False
