from func import DatabaseConnection as db
from vo.Outbound import Outbound


# 插入出库单信息
def insertOutbound(outbound):
    out_id, sale_id, goods_id, account_id, out_date, out_num, out_flag = outbound.getReturnTuple()
    key = "out_id,sale_id,goods_id,account,out_date,out_num,out_flag"
    val = f"'{out_id}','{sale_id}','{goods_id}','{account_id}','{out_date}',{out_num},'{out_flag}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_outbound", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询所有出库单
def selectOutbound():
    sql = f"SELECT DISTINCT out_id,sale_id,account,out_date FROM tb_outbound"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    outbound = []
    for item in result:
        out_id, sale_id, account, out_date = item
        outbound.append(Outbound(out_id, sale_id, account, out_date))
    return outbound


# 通过订单ID查询订单
def selectOutboundByOutboundId(out_id):
    sql = f"SELECT * FROM tb_outbound WHERE out_id='{out_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    outbound = []
    for item in result:
        out_id, sale_id, goods_id, account_id, out_date, out_num, out_flag = item
        outbound.append(Outbound(out_id, sale_id, account_id, out_date, goods_id, out_num, out_flag))
    return outbound


# 更新出库单状态为已发货
def updateOutboundFlagtoDelivered(outbound_id):
    sql = "UPDATE tb_outbound SET out_flag='已发货' WHERE out_id='{out_id}'".format(out_id=outbound_id)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找出库单信息
def selectCustomerByKeywords(outbound_id, sale_id, date_before, date_after):
    sql = f"SELECT DISTINCT out_id,sale_id,account,out_date FROM tb_outbound WHERE out_id LIKE '%{outbound_id}%' AND sale_id LIKE '%{sale_id}%' AND out_date BETWEEN '{date_before}' AND '{date_after}' "
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    outbound = []
    if result is None:
        return None
    for item in result:
        out_id, sale_id, account, out_date = item
        outbound.append(Outbound(out_id, sale_id, account, out_date))
    return outbound


if __name__ == "__main__":
    # insertOutbound(Outbound(0,1,2,3,"2022-3-23",6,"已发货"))
    # selectOutbound()
    # selectOutboundByOutboundId(2021020001)
    # updateOutboundFlagtoDelivered(2021020002)
    selectCustomerByKeywords("4","5","2021-4-30","2021-5-31")
