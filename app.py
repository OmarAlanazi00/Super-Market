
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("SuperMarket Analysis.csv")
# Title
st.title("🛒 Supermarket Sales Dashboard")

st.write(
    "Analyze supermarket sales data to identify customer behavior, product performance, and sales patterns."
)

# Dataset Overview
st.header("Dataset Overview")

st.write("Shape:", df.shape)

st.dataframe(df.head())

# Product Line Sales
st.header("Total Sales by Product Line")

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=df,
    x='Product line',
    y='Sales',
    estimator=sum,
    palette='viridis',
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

st.info("Insight: Compare product categories to identify which generates the highest revenue.")

# Branch Sales
st.header("Total Sales by Branch")

fig, ax = plt.subplots()

sns.barplot(
    data=df,
    x='Branch',
    y='Sales',
    estimator=sum,
    ax=ax
)

st.pyplot(fig)

st.info("Insight: Identify the branch with the strongest sales performance.")

# Payment Distribution
st.header("Payment Method Distribution")

payment_counts = df['Payment'].value_counts()

fig, ax = plt.subplots()

ax.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct='%1.1f%%'
)

st.pyplot(fig)

# Gender Distribution
st.header("Gender Distribution")

gender_counts = df['Gender'].value_counts()

fig, ax = plt.subplots()

ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%'
)

st.pyplot(fig)

# Rating Distribution
st.header("Customer Rating Distribution")

fig, ax = plt.subplots()

sns.histplot(
    df['Rating'],
    bins=10,
    kde=True,
    color='green',
    ax=ax
)

st.pyplot(fig)

# Correlation Matrix
st.header("Correlation Matrix")

fig, ax = plt.subplots(figsize=(8,5))

sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True,
    cmap='YlGnBu',
    ax=ax
)

st.pyplot(fig)

# Conclusion
st.header("Conclusion")

st.success(
    "The dashboard highlights customer behavior, product performance, payment preferences, and sales trends that support better business decisions."
)
