import os
from dotenv import load_dotenv
from supabase import create_client
import pandas as pd

load_dotenv()  # loads .env

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Functions to fetch tables
def fetch_table(table_name, limit=None):
    query = supabase.table(table_name).select("*")
    if limit:
        query = query.limit(limit)
    response = query.execute()
    return pd.DataFrame(response.data)
