import streamlit as st
import pandas as pd

# Title
st.title("Company and Work Title Analysis")

# Input Section
st.header("Choose Your Inputs")

# Text input for company name
company = st.text_input("Enter Company Name:")

# Text input for work title
work_title = st.text_input("Enter Work Title:")

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
