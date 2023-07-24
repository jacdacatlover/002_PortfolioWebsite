import streamlit as st

st.set_page_config(layout = "wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jacqueline Ng")
    content="""I am Jacqueline. I am a project manager in a financial institution and also a freelance programmer on python.
    """
    st.info(content)