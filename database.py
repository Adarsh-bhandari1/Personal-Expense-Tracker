import psycopg2 as pg
import os
from dotenv import load_dotenv
# Loading enviroment variables from .env file 
load_dotenv()
db_name=os.getenv("name") # Your database name 
db_user=os.getenv("user")  # Your user_name on pgadmin
db_password=os.getenv("password") # your password 
db_host=os.getenv("host") # Your host
db_port=os.getenv("port") # Your port Number 
# Function to connect with the database 
def connect_to_database():
    try:
        conn=pg.connect(dbname=db_name,user=db_user,password=db_password,host=db_host,port=db_port)
        print("Connection successfull")
        cur=conn.cursor()
        username_get=input("Enter the user name ")
        cur.execute("INSERT INTO TABLE (user_name , password_hash) VALUES (%s  )",(username_get))
        conn.commit()
        #return conn
    except Exception as e:
        print("Error")
        return None
connect_to_database
"""def close_database_connection(conn):
    if conn:
        conn.close()
        print("Connection closed ")"""