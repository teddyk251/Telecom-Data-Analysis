import sys
sys.path.append("../scripts/")
sys.path.append("../dashboard/")

import streamlit as st
from multiapp import MultiApp
from dashboard import user_overview_page, user_engagement_page, user_experience_page, user_satisfaction_page

st.set_page_config(page_title="TelCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TelCo's User Analytics

""")

# Add all your application here
app.add_app("User Overview Analysis", user_overview_page.app)
app.add_app("User Engagement Analysis", user_engagement_page.app)
app.add_app("User Experience Analysis", user_experience_page.app)
app.add_app("User Satisfaction Analysis", user_satisfaction_page.app)

# The main app
app.run()
