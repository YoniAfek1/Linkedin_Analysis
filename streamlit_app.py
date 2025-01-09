import streamlit as st
import pandas as pd
from databricks import sql

# Databricks connection details
DATABRICKS_SERVER_HOSTNAME = "adb-3738544368441327.7.azuredatabricks.net"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/574203acc747d7db"
DATABRICKS_ACCESS_TOKEN = "Yoni"  # Replace with your actual token or use secure storage

# Function to connect to Databricks and query unique company names
def get_unique_company_names():
    # Query to extract unique company names
    query = "SELECT DISTINCT company_name FROM your_table LIMIT 100"  # Replace 'your_table' with the correct table name
    try:
        with sql.connect(
            server_hostname=DATABRICKS_SERVER_HOSTNAME,
            http_path=DATABRICKS_HTTP_PATH,
            access_token=DATABRICKS_ACCESS_TOKEN
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
        # Convert the result into a Pandas DataFrame
        companies = pd.DataFrame(rows, columns=["Company Name"])
        return companies
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Streamlit App
st.title("Role Analysis")

# Fetch unique company names from the database
st.header("Choose Company")
try:
    companies_df = get_unique_company_names()
    if not companies_df.empty:
        company_list = companies_df["Company Name"].tolist()
        company = st.selectbox("Select a Company:", company_list)
    else:
        st.warning("No companies found or unable to fetch data.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Button to trigger analysis
if st.button("Analyze"):
    if 'company' in locals() and company:  # Ensure a company is selected
        st.write(f"Analyzing data for {company}...")
        # Placeholder for analysis logic
    else:
        st.warning("Please select a company.")
