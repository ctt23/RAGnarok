import streamlit as st
from components.chat_interface import chat_interface

st.set_page_config(page_title="RAGnarok", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "FAQs"])

# Main content
if page == "Home":
    st.title("RAGnarok")
    chat_interface()
elif page == "FAQs":
    st.title("FAQs")
    st.write("Here you can add some frequently asked questions and their answers.")