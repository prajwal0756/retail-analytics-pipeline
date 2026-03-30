import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_reports():

    
    os.makedirs("reports", exist_ok=True)

    
    rfm = pd.read_csv("data/rfm_segments.csv")

   
    segment_counts = rfm["Segment"].value_counts()

    plt.figure(figsize=(8, 5))
    segment_counts.plot(kind="bar")
    plt.title("Customer Segment Distribution")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)

    plt.savefig("reports/segment_distribution.png")
    plt.close()

    
    
    revenue_segment = rfm.groupby("Segment")["Monetary"].sum().sort_values()

    plt.figure(figsize=(8, 5))
    revenue_segment.plot(kind="bar")
    plt.title("Revenue Contribution by Segment")
    plt.xlabel("Segment")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    plt.savefig("reports/revenue_by_segment.png")
    plt.close()

   
    plt.figure(figsize=(8, 5))
    plt.hist(rfm["Recency"], bins=30)
    plt.title("Recency Distribution")
    plt.xlabel("Days Since Last Purchase")
    plt.ylabel("Customers")

    plt.savefig("reports/recency_distribution.png")
    plt.close()

    
    plt.figure(figsize=(8, 5))
    plt.hist(rfm["Frequency"], bins=30)
    plt.title("Frequency Distribution")
    plt.xlabel("Number of Purchases")
    plt.ylabel("Customers")

    plt.savefig("reports/frequency_distribution.png")
    plt.close()


    plt.figure(figsize=(8, 5))
    plt.hist(rfm["Monetary"], bins=30)
    plt.title("Monetary Distribution")
    plt.xlabel("Total Spend")
    plt.ylabel("Customers")

    plt.savefig("reports/monetary_distribution.png")
    plt.close()

    print("Reports Generated Successfully!")