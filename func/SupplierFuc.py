from func import DatabaseConnection as db
from vo.Supplier import Supplier


# 查询所有供应商
def selectSupplier():
    sql = f"SELECT * FROM tb_supplier"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    supplier = []
    for item in result:
        supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr, isdelete = item
        supplier.append(Supplier(supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr, isdelete))
    return supplier


# 根据供应商编号查询供应商
def selectSupplierBySupplierId(supplier_id):
    sql = f"SELECT * FROM tb_supplier WHERE supplier_id='{supplier_id}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    supplier = []
    for item in result:
        supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr, isdelete = item
        supplier.append(Supplier(supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr, isdelete))
    return supplier


# 插入供应商
def insertSupplier(supplier):
    Supplier_id,Supplier_name,Supplier_contactor,Supplier_phone,Supplier_addr = supplier.getReturnTuple()
    key = "Supplier_id,Supplier_name,Supplier_contactor,Supplier_phone,Supplier_addr"
    val = f"'{Supplier_id}','{Supplier_name}','{Supplier_contactor}','{Supplier_phone}','{Supplier_addr}'"
    sql = "INSERT INTO {table}({key}) values ({val})".format(table="tb_supplier", key=key, val=val)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 删除供应商
def deleteSupplier(supplier_id):
    sql = "UPDATE {table} SET isdelete='{isdelete}' WHERE {key}= '{id}'".format(table="tb_supplier", isdelete=1,key="supplier_id", id=supplier_id)
    conn = db.MyDbUtil()
    flag = conn.execute(sql)
    conn.close_db()
    return flag


# 通过keywords查找供应商信息
def selectSupplierByKeywords(Supplier_id, Supplier_name):
    where = f"Supplier_id LIKE '%{Supplier_id}%' AND Supplier_name LIKE '%{Supplier_name}%'"
    sql = "SELECT * FROM {table} WHERE {where}".format(table="tb_supplier", where=where)
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    supplier = []
    for item in result:
        supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr = item
        supplier.append(Supplier(supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr))
    return supplier


# 还剩三个方法没写完，分别是根据销售号查询信息selectSaleBySaleId(String sale_id)    updateSale_outNumber(Sale sale)   selectSaleByKeywords


if __name__ == "__main__":
    # selectSupplier()
    # selectSupplierBySupplierId("G0099")
    # insertSupplier(Supplier("11","中国企业","wrp","15531288427","中国"))
    # deleteSupplier("11")
    selectSupplierByKeywords("1","集团")