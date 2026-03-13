import pandas as pd
import matplotlib.pyplot as plt


def generate_reports():

    rfm = pd.read_csv("data/rfm_segments.csv")

    segment_counts = rfm["Segment"].value_counts()

    plt.figure(figsize=(8,5))

    segment_counts.plot(kind="bar")

    plt.title("Customer Segment Distribution")

    plt.savefig("reports/segment_distribution.png")

    plt.close()