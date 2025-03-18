import streamlit as st

conn = st.connection("snowflake")

@st.cache_data
def load_table():
    session = conn.session()
    return session.table("mytable").to_pandas()

df = load_table()

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")