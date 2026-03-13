import sqlite3

DB_PATH = "data/retail_analytics.db"

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn
    