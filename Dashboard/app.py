import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

st.title("Retail Analytics Dashboard")

# -----------------------------
# Load Data
# -----------------------------

conn = sqlite3.connect("data/retail_analytics.db")

df = pd.read_sql("SELECT * FROM transactions", conn)

rfm = pd.read_csv("data/rfm_segments.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")

country_filter = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

segment_filter = st.sidebar.multiselect(
    "Select Customer Segment",
    options=rfm["Segment"].unique(),
    default=rfm["Segment"].unique()
)

df = df[df["Country"].isin(country_filter)]
rfm = rfm[rfm["Segment"].isin(segment_filter)]

# -----------------------------
# KPI Metrics
# -----------------------------

st.header("Business Overview")

total_revenue = df["TotalPrice"].sum()
total_orders = df["Invoice"].nunique()
total_customers = df["CustomerID"].nunique()
aov = total_revenue / total_orders

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue (£)", round(total_revenue, 2))
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Avg Order Value (£)", round(aov, 2))

# -----------------------------
# Monthly Revenue Trend
# -----------------------------

st.header("Monthly Revenue Trend")

monthly_sales = df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].astype(str)

fig, ax = plt.subplots()

sns.lineplot(
    x="InvoiceDate",
    y="TotalPrice",
    data=monthly_sales,
    marker="o",
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------
# Customer Segment Distribution
# -----------------------------

st.header("Customer Segment Distribution")

segment_counts = rfm["Segment"].value_counts()

fig2, ax2 = plt.subplots()

sns.barplot(
    x=segment_counts.index,
    y=segment_counts.values,
    ax=ax2
)

plt.xticks(rotation=45)

st.pyplot(fig2)

# -----------------------------
# Revenue by Segment
# -----------------------------

st.header("Revenue by Customer Segment")

segment_revenue = rfm.groupby("Segment")["Monetary"].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots()

sns.barplot(
    x=segment_revenue.index,
    y=segment_revenue.values,
    ax=ax3
)

plt.xticks(rotation=45)

st.pyplot(fig3)

# -----------------------------
# Top Selling Products
# -----------------------------

st.header("Top Selling Products")

top_products = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig4, ax4 = plt.subplots()

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    ax=ax4
)

st.pyplot(fig4)

# -----------------------------
# Revenue by Country
# -----------------------------

st.header("Revenue by Country")

country_revenue = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig5, ax5 = plt.subplots()

sns.barplot(
    x=country_revenue.values,
    y=country_revenue.index,
    ax=ax5
)

st.pyplot(fig5)

# -----------------------------
# Customer Purchase Behavior
# -----------------------------

st.header("Customer Purchase Frequency Distribution")

fig6, ax6 = plt.subplots()

sns.histplot(rfm["Frequency"], bins=30, ax=ax6)

st.pyplot(fig6)

# -----------------------------
# Top Customers
# -----------------------------

st.header("Top Customers")

top_customers = rfm.sort_values("Monetary", ascending=False).head(10)

st.dataframe(top_customers)

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.markdown(
"""
Retail Analytics Pipeline Dashboard  
Built using **Python, SQLite, Pandas, Streamlit, and Seaborn**
"""
)