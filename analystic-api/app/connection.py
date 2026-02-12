from mysql import connector 
import os

host = os.getenv("SQL_HOST","localhost")
user = os.getenv("SQL_USER","root")
password = os.getenv("PASSWORD","rootpass")

def get_conn_cursor():
    try:
        conn = connector.connect(
                host=host,
                user=user,
                password=password
            )
        cursor = conn.cursor(dictionary=True)

        return (conn , cursor)
    except Exception as e:
        raise e
    
  