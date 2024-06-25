import streamlit as st
from streamlit_ace import st_ace
import sqlalchemy as sa
import pandas as pd

# Database URI construction
db_uri = f"crate://{st.secrets['db_username']}:{st.secrets['db_password']}@{st.secrets['db_host']}:{st.secrets['db_port']}?ssl=true"
engine = sa.create_engine(db_uri, echo=True)

# Function to execute the query
def execute_query():
    query = st.session_state.get('query', 'SELECT * FROM sys.summits LIMIT 10;')
    with engine.connect() as connection:
        df = pd.read_sql(sql=sa.text(query), con=connection)
    st.session_state.query_result = df

# Streamlit App Layout
st.title("Streamlit with CrateDB ")

# SQL Editor
query = st_ace(
    language="sql", 
    value='SELECT * FROM sys.summits LIMIT 10;', 
    height=200, 
    font_size=14, 
    theme="dracula", 
    keybinding="vscode"
)

# Store the query in session state
st.session_state['query'] = query

# Execute button
if st.button("Execute Query"):
    execute_query()

# Display the query result
if 'query_result' in st.session_state:
    st.write("### Query Result")
    st.table(st.session_state.query_result)
else:
    st.write("### No query executed yet")