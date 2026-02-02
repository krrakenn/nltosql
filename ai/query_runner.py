import sqlite3
import pandas as pd

DB_PATH = r"db\chinook.db"

def run_sql(sql):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

