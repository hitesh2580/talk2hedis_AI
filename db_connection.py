"""
db_connection.py
----------------
This script connects to the Supabase database and fetches data into Pandas DataFrames.
It uses credentials stored in the .env file.
"""

import os
from supabase import create_client, Client
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Supabase credentials from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_table(table_name: str, limit: int = 1000) -> pd.DataFrame:
    """
    Fetch data from a Supabase table and return it as a Pandas DataFrame.
    :param table_name: Name of the Supabase table
    :param limit: Number of records to fetch (default: 1000)
    """
    print(f"📥 Fetching data from table: {table_name}")
    response = supabase.table(table_name).select("*").limit(limit).execute()

    if not response.data:
        print(f"⚠️ No data found in table: {table_name}")
        return pd.DataFrame()

    df = pd.DataFrame(response.data)
    print(f"✅ Retrieved {len(df)} rows from {table_name}")
    return df

# --- Example Usage ---
if __name__ == "__main__":
    # Example: Fetch data from your core tables
    members_df = fetch_table("member_enrollment")
    claims_df = fetch_table("medical_claims")
    providers_df = fetch_table("provider")

    # Display sample
    print(members_df.head())
    print(claims_df.head())
    print(providers_df.head())