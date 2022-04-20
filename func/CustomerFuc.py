from func import DatabaseConnection as db
from vo.Customer import Customer


# 查询全部顾客信息
def selectCustomer():
    sql = "SELECT * FROM tb_customer"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    customer = []
    if result is None:
        return None
    for item in result:
        customer_id, customer_name, customer_phone, customer_address, isdelete = item
        customer.append(Customer(customer_id, customer_name, customer_phone, customer_address, isdelete))
    return customer


# 通过顾客编号查询顾客信息
def selectCustomerByCustomerId(customer_id):
    sql = f"SELECT * FROM tb_customer WHERE customer_id='{customer_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    customer = []
    for item in result:
        customer_id, customer_name, customer_phone, customer_address, isdelete = item
        customer.append(Customer(customer_id, customer_name, customer_phone, customer_address, isdelete))
    return customer


# 插入顾客信息
def insertCustomer(customer):
    Customer_id, Customer_name, Customer_phone, Customer_addr = customer.getReturnTuple()
    key = "Customer_id,Customer_name,Customer_phone,Customer_addr"
    val = f"'{Customer_id}','{Customer_name}','{Customer_phone}','{Customer_addr}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_customer", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 删除顾客信息
def deleteCustomer(customer_id):
    con = f"Customer_id = '{customer_id}'"
    sql = "UPDATE {table} SET isdelete={isdelete} WHERE ({con})".format(table="tb_customer", isdelete=1, con=con)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找顾客信息
def selectCustomerByKeywords(Customer_id, Customer_name):
    sql = f"SELECT * FROM tb_customer WHERE Customer_id LIKE '%{Customer_id}%' AND Customer_name LIKE '%{Customer_name}%'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    customer = []
    if result is None:
        return None
    for item in result:
        customer_id, customer_name, customer_phone, customer_address, isdelete = item
        customer.append(Customer(customer_id, customer_name, customer_phone, customer_address, isdelete))
    return customer


if __name__ == "__main__":
    selectCustomerByKeywords(1, "")
