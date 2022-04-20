from func import DatabaseConnection as db
from vo.Goods import Goods


# 查询全部商品信息
def selectGoods():
    sql = "SELECT * FROM tb_goods"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    goods = []
    if result is None:
        return None
    for item in result:
        goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete = item
        goods.append(
            Goods(goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete))
    conn.close_db()
    return goods


# 通过供应商ID查询商品
def selectGoodsBySupplierId(supplier_id):
    sql = f"SELECT * FROM tb_goods WHERE supplier_id='{supplier_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    goods = []
    if result is None:
        return None
    for item in result:
        goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete = item
        goods.append(
            Goods(goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete))
    conn.close_db()
    return goods


# 通过商品编号查询商品
def selectGoodsByGoodsId(goods_id):
    sql = f"SELECT * FROM tb_goods WHERE goods_id='{goods_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    goods = []
    if result is None:
        return None
    for item in result:
        goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete = item
        goods.append(
            Goods(goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id, isdelete))
    conn.close_db()
    return goods


# 通过商品编号修改商品库存量
def updateGoodsNumber(goods):
    goods_id = goods.getGoods_id()
    good_number = goods.getGoods_number()
    sql = f"UPDATE tb_goods SET goods_number='{good_number}' WHERE goods_id='{goods_id}'"
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 插入商品信息
def insertGoods(goods):
    goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id = goods.getReturnTuple()
    key = "goods_id,goods_name,goods_number,price_cost,price_sell,goods_unit,supplier_id"
    val = f"'{goods_id}','{goods_name}',{goods_number},'{price_cost}','{price_sell}','{goods_unit}','{supplier_id}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_goods", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 删除商品
def deleteGoods(goods_id):
    con = f"goods_id = '{goods_id}'"
    sql = "UPDATE {table} SET isdelete='{isdelete}' WHERE ({con})".format(table="tb_goods", isdelete="1", con=con)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找商品信息
def selectGoodsByKeywords(goods_id, goods_name):
    sql = f"SELECT * FROM tb_goods WHERE goods_id LIKE '%{goods_id}%' AND goods_name LIKE '%{goods_name}%'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    goods = []
    if result is None:
        return None
    for item in result:
        goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id = item
        goods.append(Goods(goods_id, goods_name, goods_number, price_cost, price_sell, goods_unit, supplier_id))
    return goods


if __name__ == "__main__":
    selectGoodsByKeywords("0", "")
