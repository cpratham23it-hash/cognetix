import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "country_wise_latest.csv")

df = pd.read_csv(csv_path)



st.title("COVID-19 Dashboard (Snapshot Data)")

# Country selector
country = st.selectbox("Select Country", df["Country/Region"].unique())

filtered = df[df["Country/Region"] == country]

st.subheader(f"COVID-19 Stats for {country}")
st.dataframe(filtered)

# Bar chart for selected country
metrics = ["Confirmed", "Deaths", "Recovered", "Active", "New cases"]
values = [filtered[m].values[0] for m in metrics]

plt.figure(figsize=(8,4))
sns.barplot(x=metrics, y=values)
plt.xticks(rotation=45)
plt.title(f"COVID-19 Snapshot Metrics – {country}")
st.pyplot(plt)
