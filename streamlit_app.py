import streamlit as st
import pandas as pd

# Title
st.title("Company and Work Title Analysis")

# Input Section
st.header("Choose Your Inputs")

# Define lists of companies and work titles
companies = ["AA", "BB", "CC"]
work_titles = ["aa", "bb", "cc"]

# Dropdown for company selection with search functionality
company = st.selectbox("Select a Company:", companies)

# Dropdown for work title selection with search functionality
work_title = st.selectbox("Select a Work Title:", work_titles)

# Button to trigger analysis
if st.button("Analyze"):
    if company and work_title:
        st.write(f"Analyzing data for {company} with the title: {work_title}...")
        
        # Placeholder for analysis logic
        results = {
            "Metric": ["Revenue", "Employee Count", "Satisfaction Score"],
            "Value": [1000000, 500, 4.5]
        }
        result_df = pd.DataFrame(results)
        st.subheader("Analysis Results")
        st.dataframe(result_df)
    else:
        st.warning("Please fill in both fields.")
