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
Create a form that asks the user to pick their favorite color using st.selectbox()
When they submit, display:

    "You selected [Color]. That's a great choice!"

Use st.form() and st.form_submit_button().
'''

import streamlit as st

with st.form("color_form"):
    color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green", "Yellow"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"You selected {color}. That's a great choice!")
