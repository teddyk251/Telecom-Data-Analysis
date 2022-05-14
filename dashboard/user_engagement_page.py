import streamlit as st
import pandas as pd
import sys
import pickle
sys.path.append("../scripts/")
sys.path.append("../data/")

@st.cache
def load_data(DATA_URL):
    data = pickle.load(open(DATA_URL, "rb"))
    return data

def app():

    # Load Saved Results Data
    data = load_data("./data/engagement_data.pkl")
    

    st.title("User Engagement analysis")

    st.header("Top 10 Users")
    st.subheader("Top 10 users per Session traffic")
    st.dataframe(data['top_ten_per_traffic'])

    st.subheader("Top 10 users per Session duration")
    st.dataframe(data['top_ten_per_duration'])


    st.subheader(f"Top 10 users per Session Frequency")
    st.dataframe(data['top_ten_per_freq'])
    
    st.subheader(f"Top 10 users per engagement metric ")
    st.dataframe(data['top_ten_customers_per_metric'])

