from mysql_connection import get_conn_cursor

conn , cursor = get_conn_cursor()


def insert_customer(conn,cursor,customer:dict):
    query = """insert into customers (customerNumber ,customerName ,contactLastName,contactFirstName,
    phone, addressLine1, addressLine2 ,city ,state ,postalCode ,country ,salesRepEmployeeNumber ,creditLimit)
    values (%s ,%s ,%s ,%s,%s ,%s ,%s ,%s,%s ,%s ,%s ,%s,%s)"""

    values = (customer["customerNumber"] , customer["customerName"] , customer["contactLastName"] , customer["contactFirstName"],
              customer["phone"] , customer["addressLine1"], customer["addressLine2"] , customer["city"] ,
              customer["state"] , customer["postalCode"] , customer["salesRepEmployeeNumber"] , customer["creditLimit"])
    
    cursor.execute(query,values)

    conn.commit()

    print("customer inserted successfuly")


def inser_order(conn,cursor,order:dict):
    query =  """insert into orders (orderNumber ,orderDate ,requiredDate ,shippedDate,status ,comments ,customerNumber)
    values (%s,%s,%s,%s,%s,%s,%s)"""

    values = (order["orderNumber"],order["orderDate"],order["requiredDate"],order["shippedDate"],
              order["status"],order["comments"],order["customerNumber"]) 
    
    cursor.execute(query,values)

    conn.commit()

    print("order inserted successfuly")


def inser_data(data:dict):
    if data["type"] == "order":
        data.pop("type")
        inser_order(conn=conn, cursor=cursor,order=data)
    else:
        data.pop("type")
        insert_customer(conn=conn,cursor=cursor,customer=data)