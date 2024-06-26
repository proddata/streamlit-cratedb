import streamlit as st
from streamlit_ace import st_ace

conn = st.connection("cratedb", type="sql")

# Function to execute the query
def execute_query():
    query = st.session_state.get('query', 'SELECT * FROM sys.summits LIMIT 10;')
    st.session_state.query_result = conn.query(query, ttl="10m")

# Streamlit App Layout
st.title("Streamlit with CrateDB ")

# SQL Editor
query = st_ace(
    language="sql", 
    value='SELECT * FROM sys.summits LIMIT 10;', 
    height=200, 
    font_size=14, 
    theme="dracula", 
    keybinding="vscode",
    auto_update=True
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