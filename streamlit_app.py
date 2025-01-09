import streamlit as st
import pandas as pd
from databricks import sql

# Databricks connection details
DATABRICKS_SERVER_HOSTNAME = "adb-3738544368441327.7.azuredatabricks.net"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/574203acc747d7db"
DATABRICKS_ACCESS_TOKEN = "Yoni"  # Replace with your actual token or use secure storage

# Function to connect to Databricks and query unique values
def get_unique_values(column_name, table_name):
    """
    Fetch unique values for a specified column from the Databricks table.
    """
    query = f"SELECT DISTINCT {column_name} FROM {table_name} LIMIT 100"
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
        values = pd.DataFrame(rows, columns=[column_name])
        return values[column_name].tolist()
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return []  # Return an empty list in case of error

# Streamlit App
st.title("Role Analysis")

# Fetch unique company names and profile names
try:
    unique_company_names = get_unique_values("company_name", "your_table")  # Replace 'your_table' with actual table name
    unique_profile_names = get_unique_values("profile_name", "your_table")  # Replace 'your_table' with actual table name

    # Display dropdowns for selecting companies and profiles
    st.header("Choose Company and Profile")
    selected_company = st.selectbox("Select a Company:", unique_company_names)
    selected_profile = st.selectbox("Select a Profile:", unique_profile_names)
except Exception as e:
    st.error(f"An error occurred: {e}")

# Button to trigger analysis
if st.button("Analyze"):
    if selected_company and selected_profile:
        st.write(f"Analyzing data for {selected_company} and {selected_profile}...")
        # Placeholder for analysis logic
    else:
        st.warning("Please select both a company and a profile.")