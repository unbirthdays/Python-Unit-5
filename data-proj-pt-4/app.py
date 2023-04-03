import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

st.title('Supermarket Store Sales, Customer and Inventory Information, & more')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv("supermarket.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
st.balloons()
data_load_state.text("Data loaded using cached data.")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

col1, col2 = st.columns(2)
col1.metric("Total Customers", f"{data.daily_customer_count.sum():,} people")
col2.metric("Total Sales", f"${data.store_sales.sum():,}")


st.subheader(":green[Top 10 Performing Stores]")
top_10 = data.sort_values('store_sales', ascending = False).drop(columns = ['items_available', 'daily_customer_count']).head(10)
st.table(data = top_10)

st.subheader(":orange[Top 5 Performing Areas]")
top_5 = data.groupby('store_area')['store_sales'].sum().sort_values(ascending = False).head(5)
st.bar_chart(top_5, height = 400)

st.subheader("Average Store Sales Overall:")
st.header(f":blue[${data.store_sales.mean().round(2):,}]")