from func import DatabaseConnection as db
from vo.DraftOrder import DraftOrder


# 插入暂存订货单信息
def insertDraftOrder(draftorder):
    draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date, isfinish, isdelete = draftorder.getReturnTuple()
    key = "draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date"
    val = f"'{draftorder_id}','{sale_id}','{goods_id}','{order_num}','{supplier_id}','{account_id}','{date}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_draftorder", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 查询全部发货单
def selectDraftOrder():
    sql = "SELECT DISTINCT draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date, isfinish, isdelete FROM tb_draftorder "
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    draftorder = []
    if result is None:
        return None
    for item in result:
        draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date, isfinish, isdelete = item
        draftorder.append(
            DraftOrder(draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date, isfinish, isdelete))
    return draftorder


# 删除采购单信息
def deletedraftorder(draftorder_id):
    con = f"draftorder_id = '{draftorder_id}'"
    sql = "UPDATE {table} SET isdelete={isdelete} WHERE ({con})".format(table="tb_draftorder", isdelete=1, con=con)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 设置暂存采购单已完成
def setDraftOrderfinished(draftorder_id):
    con = f"draftorder_id = '{draftorder_id}'"
    sql = "UPDATE {table} SET isfinish={isfinish} WHERE ({con})".format(table="tb_draftorder", isfinish=1, con=con)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


if __name__ == "__main__":
    # insertDraftOrder(DraftOrder(0, 0, 0, 0, 0, "2022-04-28"))
    selectDraftOrder()
    deletedraftorder(0)
    setDraftOrderfinished(0)
