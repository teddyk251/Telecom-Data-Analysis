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
    data = load_data("./data/satisfaction_data.pkl")
    

    st.title("User Satisfaction analysis")

    st.subheader("Top 10 Most Satisfied Users")
    st.dataframe(data['top_10_satisfied'])
