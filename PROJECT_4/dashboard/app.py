import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "OnlineRetail.csv")

df = pd.read_csv(csv_path, encoding="ISO-8859-1")

df = df.dropna()
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Month"] = df["InvoiceDate"].dt.to_period("M")

st.title("🛒 Online Retail Dashboard")

st.metric("Total Revenue", f"{df['Revenue'].sum():,.2f}")
st.metric("Total Orders", df["InvoiceNo"].nunique())

top_products = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False)

st.subheader("Top 10 Products")
st.bar_chart(top_products.head(10))

monthly_revenue = df.groupby("Month")["Revenue"].sum()
st.subheader("Monthly Revenue")
st.line_chart(monthly_revenue)
