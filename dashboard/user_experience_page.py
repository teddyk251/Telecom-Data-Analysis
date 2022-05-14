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
    data = load_data("./data/experience_data.pkl")
    

    st.title("User Experience analysis")

    # st.header("Overall Handset Manufacturers and Type Data")
    st.subheader("Top 10 TCP Retransmission Values")
    st.dataframe(data['top_10_tcp'])

    st.subheader("Bottom 10 TCP Retransmission Values")
    st.dataframe(data['bottom_10_tcp'])

    st.subheader("Top 10 RTT Values")
    st.dataframe(data['top_10_rtt'])

    st.subheader("Bottom 10 RTT Values")
    st.dataframe(data['bottom_10_rtt'])

    st.subheader("Top 10 Throughput  Values")
    st.dataframe(data['top_10_tp'])

    st.subheader("Bottom 10 Throughput Values")
    st.dataframe(data['bottom_10_tp'])

    st.subheader("User Cluster per Experience Metric ")
    st.dataframe(data['cluster'])
    body = """ #### Cluster 0
* This cluster of users have the worst experience as compared to the other cluster. They have the highest RTT and TCP retransmission on average which indicates that there is less throughput. This can be confirmed by comparing the mean values. This cluster also contains the highest number of users. 



#### Cluster 1
* Users in cluster 1 have the best experience. They have less delay(smaller RTT) and also less tcp retransmission which indicates that the majority of the traffic is successfully sent and recieved. This means there is high throughput and this can be confirmed by the mean values. This cluster contains the smallest number of users.


#### Cluster 2
* Users in cluster 2 have an intermediate experience. They have an experience which is closer to cluster 1 meaning they have an experience that is slightly worse than cluster 1.
"""
    st.markdown(body)
