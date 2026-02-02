from groq import Groq
from ai.schema_context import SCHEMA_CONTEXT

def generate_sql(user_prompt):
    api_key = "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"
    client = Groq(api_key=api_key)

    prompt = f"""
You are a SQLite expert.
Use ONLY this schema.

{SCHEMA_CONTEXT}

Question:
{user_prompt}

also double check the SQL syntax for SQLite compatibility and with schema/database compatibility.

Return only SQL.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql = completion.choices[0].message.content.strip()
    # remove markdown if present
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

# print(generate_sql(
#     "Show cashew products where Grade is filled grouped by seller type"
# ))

# from ai.query_runner import run_sql

# user_q = "Show top 10 countries by total sales"
# sql = generate_sql(user_q)

# print("Generated SQL:\n", sql)
# print("\nResult:")
# print(run_sql(sql))