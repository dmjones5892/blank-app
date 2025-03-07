import streamlit as st
from Views.AddPostView import AddPostView
from Views import FeedView
from Services import get_feed, add_post
AddPostView(add_post)
st.write("___")
FeedView(get_feed)