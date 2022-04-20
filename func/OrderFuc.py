from func import DatabaseConnection as db
from vo.Order import Order


# 插入采购单信息
def insertOrder(order):
    order_id, account_id, supplier_id, order_left, order_date, goods_id, order_flag, order_number = order.getReturnTuple()
    key = "order_id,account,Supplier_id,order_left,order_date,goods_id,order_flag,order_number"
    val = f"'{order_id}','{account_id}','{supplier_id}',{order_left}," \
          f"'{order_date}','{goods_id}','{order_flag}',{order_number}"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_order", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询所有订单
def selectOrder():
    sql = f"SELECT DISTINCT order_id,account,Supplier_id,order_date FROM tb_order"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    order = []
    for item in result:
        order_id, account_id, supplier_id, order_date = item
        order.append(Order(order_id=order_id, account_id=account_id, supplier_id=supplier_id, order_date=order_date))
    return order


# 通过订单ID查询订单
def selectOrderByOrderId(order_id):
    sql = f"SELECT * FROM tb_order WHERE order_id='{order_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    order = []
    for item in result:
        order_id, account_id, supplier_id, order_left, order_date, goods_id, order_flag, order_number = item
        order.append(Order(order_id=order_id, account_id=account_id, supplier_id=supplier_id, order_date=order_date, goods_id=goods_id, order_flag=order_flag,
                           order_number=order_number, order_left=order_left))
    return order


# 更新订单Flag
def updateOrderFlag(order):
    sql = f"UPDATE tb_order SET order_left={order.get_order_left()},order_flag='{order.get_order_flag()}' " \
          f"WHERE order_id='{order.get_order_id()}' and goods_id='{order.get_goods_id()}'"
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找顾客信息
def selectOrderByKeywords(order_id, supplier_id, date_front, date_after):
    # 小的时间要在前面
    sql = f"SELECT DISTINCT order_id,account,Supplier_id,order_date FROM tb_order WHERE order_id LIKE '%{order_id}%' AND supplier_id LIKE '%{supplier_id}%' AND order_date BETWEEN '{date_front}' AND '{date_after}' "
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    order = []
    if result is None:
        return None
    for item in result:
        order_id, account, Supplier_id, order_date = item
        order.append(Order(order_id=order_id, account_id=account, supplier_id=Supplier_id, order_date=order_date))
    return order


if __name__ == "__main__":
    # insertOrder(Order(1, 2, 3, 4, "2001-5-5", 6, 7, 8, 9))
    # selectOrder()
    # selectOrderByOrderId("2021040001")
    # updateOrderFlag(Order(1, 2, 3, "2022-3-23", goods_id=6, order_left=10, order_flag="未出库"))
    selectOrderByKeywords("3",'0','2021-04-30','2021-06-30')
