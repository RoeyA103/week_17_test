from mysql import connector 

def get_conn_cursor(host,user,password):
    try:
        conn = connector.connect(
                host=host,
                user=user,
                password=password
            )
        cursor = conn.cursor()

        cursor.execute(f"USE test17")




        return (conn , cursor)
    except Exception as e:
        raise e