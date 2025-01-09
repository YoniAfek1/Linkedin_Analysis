pip install databricks-sql-connector

import streamlit as st
import pandas as pd
from databricks import sql

# Databricks connection details
DATABRICKS_SERVER_HOSTNAME = "adb-3738544368441327.7.azuredatabricks.net"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/574203acc747d7db"
DATABRICKS_ACCESS_TOKEN = "Yoni"

# Function to connect to Databricks and query data
def get_companies_from_db():
    query = "SELECT DISTINCT company_name FROM your_table LIMIT 100"  # Adjust query as needed
    with sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_ACCESS_TOKEN
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
    # Convert rows to a Pandas DataFrame
    companies = pd.DataFrame(rows, columns=["Company Name"])
    return companies

# Streamlit App
st.title("Role Analysis")

# Fetch companies from Databricks
st.header("Choose Company")
try:
    companies_df = get_companies_from_db()
    company_list = companies_df["Company Name"].tolist()
    company = st.selectbox("Select a Company:", company_list)
except Exception as e:
    st.error(f"Error connecting to Databricks: {e}")

# Button to trigger analysis
if st.button("Analyze"):
    if company:
        st.write(f"Analyzing data for {company}...")
        # Placeholder for analysis logic
    else:
        st.warning("Please select a company.")
