from func import DatabaseConnection as db
from vo.Sale import Sale


# 插入销售单
def insertSale(sale):
    sale_id, account_id, customer_id, goods_id, sale_date, sale_number, sale_left, sale_flag = sale.getReturnTuple()
    key = "sale_id,account_id,customer_id,goods_id,sale_date,sale_number,sale_left,sale_flag"
    val = f"'{sale_id}','{account_id}','{customer_id}','{goods_id}','{sale_date}',{sale_number},{sale_left},'{sale_flag}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_sale", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询所有销售单
def selectSale():
    sql = f"SELECT DISTINCT sale_id,account_id,customer_id,sale_date FROM tb_sale"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    sale = []
    for item in result:
        sale_id, account_id, customer_id, sale_date = item
        sale.append(Sale(sale_id, account_id, customer_id, sale_date))
    if sale is None: sale = []
    return sale


# 根据销售号查询信息
def selectSaleBySaleId(sale_id):
    sql = f"SELECT * FROM tb_sale WHERE sale_id='{sale_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    sale = []
    for item in result:
        sale_id, account_id, customer_id, goods_id, sale_date, sale_number, sale_left, sale_flag = item
        sale.append(Sale(sale_id, account_id, customer_id, sale_date, goods_id, sale_number, sale_left, sale_flag))
    if sale is None: sale = []
    return sale


# 更新销售单的已发货数量和出库flag
def updateSale_outNumber(sale):
    sale_id, account_id, customer_id, goods_id, sale_date, sale_number, sale_left, sale_flag = sale.getReturnTuple()
    set = f"sale_left={sale_left},sale_flag='{sale_flag}'"
    where = f"sale_id='{sale_id}' and goods_id='{goods_id}'"
    sql = "UPDATE {table} SET {set} WHERE {where}".format(table="tb_sale", set=set, where=where)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找销售单信息
def selectSaleByKeywords(sale_id, customer_id, date_before, date_after):
    key = f"sale_id,account_id,customer_id,sale_date"
    where = f"sale_id LIKE '%{sale_id}%' AND Customer_id LIKE '%{customer_id}%' AND sale_date BETWEEN '{date_before}' AND '{date_after}' "
    sql = "SELECT DISTINCT {key} FROM {table} WHERE {where}".format(table="tb_sale", key=key, where=where)
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    sale = []
    if result is None:
        return None
    for item in result:
        sale_id, account_id, customer_id, sale_date = item
        sale.append(Sale(sale_id, account_id, customer_id, sale_date))
    if sale is None: sale = []
    return sale


if __name__ == "__main__":
    # insertSale(Sale(0,1,2,3,"2022-3-23",5,6,7))
    # selectSale()
    # selectSaleBySaleId(2021010001)
    # updateSale_outNumber(Sale(sale_id="2021010001",goods_id="P0003GI",sale_left="10",sale_flag="未出库数量：10"))
    selectSaleByKeywords("2", "5", "2021-4-30", "2021-5-20")
