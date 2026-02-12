from connection import get_conn_cursor


def get_top_customers():

    conn , cursor = get_conn_cursor()

    cursor.execute(f"USE test17")

    query = """SELECT *  FROM customers 
                right join (select customerNumber from orders group by customerNumber order by count(customerNumber) desc limit 10) new
                on new.customerNumber = customers.customerNumber"""

   

    cursor.execute(query)

    res = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return res


def get_customerswithout_orders():
    pass


def get_zero_credit_active_customers():
    pass
