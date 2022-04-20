from func import DatabaseConnection as db
from vo.Purchase import Purchase


# 插入采购单信息
def insertPurchase(purchase):
    pur_id, account_id, sale_id, goods_id, pur_date, pur_number = purchase.getReturnTuple()
    key = "pur_id,account,sale_order,goodsid,pur_date,pur_number"
    val = f"'{pur_id}','{account_id}','{sale_id}','{goods_id}','{pur_date}',{pur_number}"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_purchase", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


if __name__ == "__main__":
    insertPurchase(Purchase(0,0,0,0,"2022-3-23",0))
