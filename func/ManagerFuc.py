from func import DatabaseConnection as db
from vo.Manager import Manager


# 通过会员账号查询用户
def selectManagerByAccount(account):
    sql = f"SELECT * FROM tb_manager WHERE account='{account}'"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    manager = []
    for item in result:
        account, password, manager_name, department = item
        manager.append(Manager(account, password, manager_name, department))
    return manager


# 查询所有会员
def selectManager():
    sql = f"SELECT * FROM tb_manager"
    conn = db.MyDbUtil()
    result = conn.query_sql(sql)
    conn.close_db()
    if result is None:
        return None
    manager = []
    for item in result:
        account, password, manager_name, department = item
        manager.append(Manager(account, password, manager_name, department))
    return manager


if __name__ == "__main__":
    selectManagerByAccount("1")
    selectManager()