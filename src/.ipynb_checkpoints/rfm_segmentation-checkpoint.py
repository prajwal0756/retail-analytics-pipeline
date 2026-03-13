import pandas as pd
from database import create_connection


def calculate_rfm():

    conn = create_connection()

    df = pd.read_sql("SELECT * FROM transactions", conn)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    snapshot_date = df["InvoiceDate"].max()

    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "Invoice": "count",
        "TotalPrice": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    rfm.to_csv("data/rfm_segments.csv")

    conn.close()

    return rfm