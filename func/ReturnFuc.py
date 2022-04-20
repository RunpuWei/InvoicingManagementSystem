from func import DatabaseConnection as db
from vo.Return import Return


# 插入退货单信息
def insertReturn(re):
    re_id, account_id, order_id, goods_id, re_date = re.getReturnTuple()
    key = "re_id,account,order_id,goods_id,re_date"
    val = f"'{re_id}','{account_id}','{order_id}','{goods_id}','{re_date}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_return", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询所有退货单
def selectReturn():
    sql = f"SELECT DISTINCT re_id,account,order_id,re_date FROM tb_return"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    re = []
    for item in result:
        re_id, account, order_id, re_date = item
        re.append(Return(re_id, account, order_id, re_date))
    return re


# 通过退货单ID查询退货单
def selectReturnByReturnId(return_id):
    sql = f"SELECT * FROM tb_return WHERE re_id='{return_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    re = []
    for item in result:
        re_id, account, order_id, goods_id, re_date = item
        re.append(Return(re_id, account, order_id, re_date, goods_id))
    return re


if __name__ == "__main__":
    # insertReturn(Return(0,0,0,0,"2022-3-23"))
    # selectReturn()
    selectReturnByReturnId(2021050001)
