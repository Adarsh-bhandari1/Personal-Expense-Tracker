import psycopg2 as pg
import os
from dotenv import load_dotenv
# Loading enviroment variables from .env file 
load_dotenv()
name=os.getenv("name")
user=os.getenv("user")
password=os.getenv("password")
host=os.getenv("host")
port=os.getenv("port")
# Function to connect with the database 
def connect_to_database():
    try:
        conn=pg.connect(dbname=name,user=user,password=password,host=host,port=port)
        print("Connected to database successfully")
        return conn
    except Exception as e:
        print("Connection failed ")
        return None
connect_to_database()
