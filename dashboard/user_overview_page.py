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
    data = load_data("./data/overview_data.pkl")
    

    st.title("User Overview analysis")

    st.header("Overall Handset Manufacturers and Type Data")
    st.subheader("Top 10 Handsets used by customers")
    st.dataframe(data['top_ten_handset'])

    st.subheader("Top 3 Handsets Manufacturers")
    st.dataframe(data['top_three_handset_manufacturer'])


    st.subheader(f"Top 5 Handsets Made by Samsung")
    st.dataframe(data['top_five_samsung_handset_type'])
    
    st.subheader(f"Top 5 Handsets Made by Apple")
    st.dataframe(data['top_five_apple_handset_type'])

    st.subheader(f"Top 5 Handsets Made by Huawei")
    st.dataframe(data['top_five_huawei_handset_type'])
