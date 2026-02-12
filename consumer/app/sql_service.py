from mysql_connection import get_conn_cursor
import os
# FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
conn , cursor = get_conn_cursor()


def int_db(conn,cursor):

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS test17")
    print(f"Database 'test17' ensured.")


    cursor.execute(f"USE test17")

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customerNumber int PRIMARY KEY,
        customerName varchar(255),
        contactLastName varchar(255),
        contactFirstName  varchar(255),
        phone varchar(255),
        addressLine1 varchar(255),
        addressLine2 varchar(255),
        city varchar(255),
        state varchar(255),
        postalCode varchar(255),
        country varchar(255),
        salesRepEmployeeNumber int,
        creditLimit float
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        orderNumber int,
        orderDate varchar(255),
        requiredDate varchar(255),
        shippedDate varchar(255),
        status varchar(255),
        comments varchar(255),
        customerNumber int
    )
    """)


    conn.commit()
    cursor.close()
    conn.close()
    print("Tables 'customers' and 'orders' ensured in database.")  

def insert_customer(conn,cursor,customer:dict):
    try:
        cursor.execute("USE test17")

        query = """insert into customers (customerNumber ,customerName ,contactLastName,contactFirstName,
        phone, addressLine1, addressLine2 ,city ,state ,postalCode ,country ,salesRepEmployeeNumber ,creditLimit)
        values (%s ,%s ,%s ,%s,%s ,%s ,%s ,%s,%s ,%s ,%s ,%s,%s)"""

        values = (customer["customerNumber"] , customer["customerName"] , customer["contactLastName"] , customer["contactFirstName"],
                customer["phone"] , customer["addressLine1"], customer["addressLine2"] , customer["city"] ,
                customer["state"] , customer["postalCode"] ,customer["country"], customer["salesRepEmployeeNumber"] , customer["creditLimit"])
    
        cursor.execute(query,values)

        conn.commit()
        cursor.close()
        conn.close()
    except KeyError:
        pass

    print("customer inserted successfuly")


def inser_order(conn,cursor,order:dict):
    try:
        cursor.execute("USE test17")

        query =  """insert into orders (orderNumber ,orderDate ,requiredDate ,shippedDate,status ,comments ,customerNumber)
        values (%s,%s,%s,%s,%s,%s,%s)"""

        values = (order["orderNumber"],order["orderDate"],order["requiredDate"],order["shippedDate"],
                order["status"],order["comments"],order["customerNumber"]) 
        
        cursor.execute(query,values)

        conn.commit()
        cursor.close()
        conn.close()
    except KeyError:
        pass

    print("order inserted successfuly")


def inser_data(data:dict):
    conn , cursor = get_conn_cursor()
    if data["type"] == "order":
        data.pop("type")
        inser_order(conn=conn, cursor=cursor,order=data)
    else:
        data.pop("type")
        insert_customer(conn=conn,cursor=cursor,customer=data)