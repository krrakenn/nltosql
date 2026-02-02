import streamlit as st
from ai.sql_generator import generate_sql
from ai.query_runner import run_sql

st.title("Talk to Your Data Warehouse")

MAX_RETRIES = 3

user_prompt = st.text_input("Ask a valid and legit question about the data")

if st.button("Run"):
    if not user_prompt:
        st.warning("Please enter a question")
        st.stop()

    attempt = 0
    last_error = None

    while attempt < MAX_RETRIES:
        attempt += 1

        with st.spinner(f"Generating SQL (attempt {attempt})..."):
            if last_error:
                prompt = f"""
User question:
{user_prompt}

Previous SQL error:
{last_error}

Generate a corrected SQLite SQL query.
Return only SQL.
"""
            else:
                prompt = user_prompt

            sql = generate_sql(prompt)

        try:
            result = run_sql(sql)

            st.subheader("Result")
            st.dataframe(result)
            st.success(f"Query succeeded on attempt {attempt}")
            break

        except Exception as e:
            last_error = str(e)
            st.error(f"Attempt {attempt} failed:")
            st.error(last_error)

    else:
        st.error("All retry attempts failed. Please refine the question.")
