import streamlit as st


st.set_page_config(page_title="Multipage App", page_icon="👋")

st.write("# Welcome to the multipage app! 👋")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    This small app follows Streamlit's folder-based multipage pattern.

    **👈 Select a page from the sidebar** to explore the two example pages.
    """
)
