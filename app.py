import sys
sys.path.append("../scripts/")
sys.path.append("../dashboard/")

import streamlit as st
from multiapp import MultiApp
from dashboard import user_overview_page
# , user_engagement_analysis_page, user_experience_analysis_page , user_satisfaction_analysis_page, model_implementation
# import your app modules here

st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
### Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access
\t- Presentation changed to SideBar
""")

# Add all your application here
app.add_app("User Overview Analysis", user_overview_page.app)
# app.add_app("User Engagement Analysis", user_engagement_analysis_page.app)
# app.add_app("User Experience Analysis", user_experience_analysis_page.app)
# app.add_app("User Satisfaction Analysis", user_satisfaction_analysis_page.app)
# app.add_app("Predict Satisfaction", model_implementation.app)

# The main app
app.run()
