import streamlit as st


st.set_page_config(page_title="Page One", page_icon="1️⃣")

st.title("Page One")
st.write("This is the first page in the multipage Streamlit app.")

number = st.slider("Choose a number", min_value=0, max_value=10, value=5)
st.write(f"You selected **{number}**.")
