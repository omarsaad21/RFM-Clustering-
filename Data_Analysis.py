import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (using your file paths)
@st.cache
def load_data():
    transactions = pd.read_csv("D:\Epsilon AI internship\Project 2\Transactions.csv")
    categories = pd.read_csv("D:\Epsilon AI internship\Project 2\Categories.csv")
    return transactions, categories

# Load data
transactions, categories = load_data()

# Summary of the Data Analysis
st.title("Data Analysis Summary")

st.markdown("""
### Summary:
In this section, we will explore the transactions and categories data to gain insights into user behavior and purchasing patterns.
We will analyze the frequency of transactions, total amounts spent by users, popular categories, and other key metrics.
The insights will help us understand the data better and prepare for customer segmentation.
""")

# Displaying the head of the datasets
st.subheader("Transactions Dataset")
st.write(transactions.head())

st.subheader("Categories Dataset")
st.write(categories.head())

# Add a few charts as representative analysis


# Bar chart: Count of merchants by category
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=categories, palette='viridis')
plt.title('Count of Merchants by Category')
plt.xticks(rotation=45)

# Render the chart in Streamlit
st.pyplot(plt)


# Bar chart: Distribution of transactions by merchant
plt.figure(figsize=(10, 6))
sns.countplot(y='MerchantName', data=transactions, order=transactions['MerchantName'].value_counts().index, palette='plasma')
plt.title('Transaction Count by Merchant')

# Render the chart in Streamlit
st.pyplot(plt)


# Histogram: Distribution of transaction values
plt.figure(figsize=(10, 6))
sns.histplot(transactions['TransactionValue'], bins=30, kde=True, color='blue')
plt.title('Distribution of Transaction Values')
plt.xlabel('Transaction Value')

# Render the chart in Streamlit
st.pyplot(plt)


# Scatter Plot: Transaction Value vs Redeemed Points
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TransactionValue', y='TransactionRedeemedPoints', data=transactions, hue='MerchantName', palette='cool')
plt.title('Transaction Value vs Redeemed Points')
plt.xlabel('Transaction Value')
plt.ylabel('Redeemed Points')

# Render the chart in Streamlit
st.pyplot(plt)

