import pandas as pd
from database import create_connection


def calculate_rfm():

    conn = create_connection()

    df = pd.read_sql("SELECT * FROM transactions", conn)

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    snapshot_date = df["InvoiceDate"].max()

    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "Invoice": "nunique",
        "TotalPrice": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    rfm = rfm.reset_index()

    # Create RFM scores
    rfm["R_score"] = pd.qcut(rfm["Recency"], 4, labels=[4,3,2,1])
    rfm["F_score"] = pd.qcut(rfm["Frequency"], 4, labels=[1,2,3,4])
    rfm["M_score"] = pd.qcut(rfm["Monetary"], 4, labels=[1,2,3,4])

    rfm["RFM_Score"] = (
        rfm["R_score"].astype(str) +
        rfm["F_score"].astype(str) +
        rfm["M_score"].astype(str)
    )

    # Segment customers
    def segment_customer(row):

        if row["RFM_Score"] == "444":
            return "Champions"

        elif row["F_score"] >= 3 and row["M_score"] >= 3:
            return "Loyal Customers"

        elif row["R_score"] == 4:
            return "Recent Customers"

        elif row["R_score"] == 1:
            return "At Risk"

        else:
            return "Others"

    rfm["Segment"] = rfm.apply(segment_customer, axis=1)

    rfm.to_csv("data/rfm_segments.csv", index=False)

    conn.close()

    return rfm