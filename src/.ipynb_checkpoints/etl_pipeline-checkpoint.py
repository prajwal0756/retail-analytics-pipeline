import pandas as pd
from src.database import create_connection


def extract_data():

    df = pd.read_csv("data/OnlineRetail.csv")

    return df


def transform_data(df):

    
    df.columns = df.columns.str.strip().str.replace(" ", "")
    
    
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    
    df = df.dropna(subset=["CustomerID"])

    
    df["TotalPrice"] = df["Quantity"] * df["Price"]

    return df


def load_data(df):

    conn = create_connection()

    df.to_sql(
        "transactions",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def run_etl():

    df = extract_data()

    df = transform_data(df)

    load_data(df)

    return df
