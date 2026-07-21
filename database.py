#Its one and only job is to connect to the database.
import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2 #Python needs someone that speaks PostgreSQL.

def get_database_connection():
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT")
    
    try:
        connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    
        return connection
     
    except Exception as e:
         print("Connection is failing. Try checking the logs or variables value")
         print(e)
         return None



