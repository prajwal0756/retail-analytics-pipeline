import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")


sns.set_style("whitegrid")
plt.rcParams.update({"font.size": 8})

st.title("Retail Analytics Dashboard")

conn = sqlite3.connect("data/retail_analytics.db")

df = pd.read_sql("SELECT * FROM transactions", conn)
rfm = pd.read_csv("data/rfm_segments.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


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


st.header("Business Overview")

total_revenue = df["TotalPrice"].sum()
total_orders = df["Invoice"].nunique()
total_customers = df["CustomerID"].nunique()
aov = total_revenue / total_orders if total_orders != 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue (£)", f"{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Avg Order Value (£)", f"{aov:,.2f}")


monthly_sales = df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"].sum().reset_index()
monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].astype(str)

fig1, ax1 = plt.subplots(figsize=(6,3))

sns.lineplot(
    x="InvoiceDate",
    y="TotalPrice",
    data=monthly_sales,
    marker="o",
    ax=ax1
)

ax1.set_title("Monthly Revenue")
ax1.tick_params(axis='x', rotation=45)


segment_counts = rfm["Segment"].value_counts()

fig2, ax2 = plt.subplots(figsize=(6,3))

sns.barplot(
    x=segment_counts.index,
    y=segment_counts.values,
    ax=ax2
)

ax2.set_title("Customer Segments")
ax2.tick_params(axis='x', rotation=45)

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1, use_container_width=True)

with col2:
    st.pyplot(fig2, use_container_width=True)


segment_revenue = rfm.groupby("Segment")["Monetary"].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(6,3))

sns.barplot(
    x=segment_revenue.index,
    y=segment_revenue.values,
    ax=ax3
)

ax3.set_title("Revenue by Segment")
ax3.tick_params(axis='x', rotation=45)


country_revenue = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig4, ax4 = plt.subplots(figsize=(6,3))

sns.barplot(
    x=country_revenue.values,
    y=country_revenue.index,
    ax=ax4
)

ax4.set_title("Top Countries by Revenue")




col3, col4 = st.columns(2)

with col3:
    st.pyplot(fig3, use_container_width=True)

with col4:
    st.pyplot(fig4, use_container_width=True)


top_products = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig5, ax5 = plt.subplots(figsize=(6,3))

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    ax=ax5
)

ax5.set_title("Top Selling Products")


fig6, ax6 = plt.subplots(figsize=(6,3))

sns.histplot(rfm["Frequency"], bins=30, ax=ax6)

ax6.set_title("No.of Purchase")



col5, col6 = st.columns(2)

with col5:
    st.pyplot(fig5, use_container_width=True)

with col6:
    st.pyplot(fig6, use_container_width=True)


st.header("Top Customers")

top_customers = rfm.sort_values("Monetary", ascending=False).head(10)

st.dataframe(top_customers, use_container_width=True)



import os
import streamlit as st

st.header(" Pipeline Monitoring")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "scheduler.log")

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()

    if logs:  
        st.subheader("Recent Pipeline Logs")
        st.text("".join(logs[-10:]))
    else:
        st.warning("Log file exists but is empty — run the pipeline first")
else:
    st.warning(f"No log file found at: {log_file}")  


import datetime

if os.path.exists(log_file):
    last_modified = os.path.getmtime(log_file)
    last_run = datetime.datetime.fromtimestamp(last_modified)

    st.metric("Last Pipeline Run", last_run.strftime("%Y-%m-%d %H:%M:%S"))


if logs and "ERROR" in logs[-1]:
    st.error("Pipeline Status: Failed ")
else:
    st.success("Pipeline Status: Running Successfully ")



st.markdown("---")

st.markdown(
"""
**Retail Analytics Pipeline Dashboard**  
Built using **Python, SQLite, Pandas, Streamlit, and Seaborn**
"""
)

conn.close()