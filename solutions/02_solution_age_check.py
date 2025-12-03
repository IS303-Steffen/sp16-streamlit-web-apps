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
Ask the user to enter their name and age. If they’re 18 or older, display:

    "Welcome, [Name]. You are an adult."

Otherwise, display:

    "Sorry, [Name]. You must be at least 18."

Use st.text_input() and st.number_input().
'''

import streamlit as st

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)

if name:
    if age >= 18:
        st.write(f"Welcome, {name}. You are an adult.")
    else:
        st.write(f"Sorry, {name}. You must be at least 18.")
