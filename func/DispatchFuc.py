from func import DatabaseConnection as db
from vo.Dispatch import Dispatch
import time


# 插入发货单信息
def insertDispatch(dispatch):
    dispatch_id, account_id, out_id, disp_date = dispatch.getReturnTuple()
    key = "disp_id, account, out_id, disp_date"
    val = f"'{dispatch_id}','{account_id}','{out_id}','{disp_date}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_dispatch", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询全部发货单
def selectDispatch():
    sql = "SELECT DISTINCT disp_id,account,out_id,disp_date FROM tb_dispatch "
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    dispatch = []
    if result is None:
        return None
    for item in result:
        dispatch_id, account_id, out_id, disp_date = item
        dispatch.append(Dispatch(dispatch_id, account_id, out_id, disp_date))
    return dispatch


# 通过发货单ID查询发货单
def selectDispatchByDispatchId(Disp_id):
    sql = f"SELECT * FROM tb_Dispatch WHERE Disp_id='{Disp_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    dispatch = []
    if result is None:
        return None
    for item in result:
        dispatch_id, account_id, out_id, disp_date = item
        dispatch.append(Dispatch(dispatch_id, account_id, out_id, disp_date))
    return dispatch


if __name__ == "__main__":
    selectDispatchByDispatchId(0)