import streamlit as st
from services.gpt_service import get_gpt_response

def chat_interface():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("Ask me any security questions, and I will try to answer them!")

    for message in st.session_state.messages:
        st.write(message)

    user_input = st.text_input("You: ", key="input")

    if st.button("Send"):
        if user_input:
            st.session_state.messages.append(f"You: {user_input}")
            response = get_gpt_response(user_input)
            st.session_state.messages.append(f"GPT-4: {response}")
            st.experimental_rerun()