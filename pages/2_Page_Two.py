import streamlit as st


st.set_page_config(page_title="Page Two", page_icon="2️⃣")

st.title("Page Two")
st.write("This is the second page in the multipage Streamlit app.")

name = st.text_input("What is your name?", placeholder="Enter your name")
if name:
    st.success(f"Hello, {name}!")
