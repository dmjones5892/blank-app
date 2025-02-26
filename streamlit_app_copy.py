import streamlit as st

st.set_page_config(

    page_title='The Dave Jones World',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **The Dave Jones World**'
        }
)
st.sidebar.title('The Dave Jones World')
st.title('The Dave Jones World')

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("David Jones is creating this app.")