import psycopg2 as pg
import os
from dotenv import load_dotenv
# Loading enviroment variables from .env file 
load_dotenv()
db_name=os.getenv("name")
db_user=os.getenv("user")
db_password=os.getenv("password")
db_host=os.getenv("host")
db_port=os.getenv("port")
# Function to connect with the database 
def connect_to_database():
    try:
        conn=pg.connect(dbname=db_name,user=db_user,password=db_password,host=db_host,port=db_port)
        print("Connected to database successfully")
        return conn
    except Exception as e:
        print("Connection failed ")
        return None
