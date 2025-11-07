import streamlit as st

st.set_page_config(page_title="Hello App", page_icon="👋")

st.title("👋 Welcome to My Streamlit App!")
name = st.text_input("What’s your name?")
mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😐 Okay", "😞 Sad"])

if st.button("Submit"):
    if name:
        st.success(f"Hey {name}! It’s nice to know you’re feeling {mood}.")
    else:
        st.warning("Please enter your name before submitting!")
