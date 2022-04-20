from func import DatabaseConnection as db
from vo.Inbound import Inbound


# 插入入库单信息
def insertInbound(inbound):
    in_id, order_id, goods_id, account_id, in_date, in_num = inbound.getReturnTuple()
    key = "in_id, order_id, goods_id, account, in_date, in_num"
    val = f"'{in_id}','{order_id}','{goods_id}','{account_id}','{in_date}','{in_num}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_inbound", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询全部入库单
def selectInbound():
    sql = f"SELECT DISTINCT in_id,order_id,account,in_date FROM tb_inbound"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    inbound = []
    for item in result:
        in_id, order_id, account_id, in_date = item
        inbound.append(Inbound(in_id, order_id, account_id=account_id, in_date=in_date))
    return inbound


# 通过入库ID查询全部入库单
def selectInboundByInboundId(inbound_id):
    sql = f"SELECT * FROM tb_inbound WHERE in_id='{inbound_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    inbound = []
    for item in result:
        in_id, order_id, goods_id, account_id, in_date, in_num = item
        inbound.append(Inbound(in_id, order_id, goods_id, account_id, in_date, in_num))
    return inbound


if __name__ == "__main__":
    insertInbound(Inbound(0,0,0,0,"2000-00-00",0,))
    selectInbound()
    selectInboundByInboundId("0")