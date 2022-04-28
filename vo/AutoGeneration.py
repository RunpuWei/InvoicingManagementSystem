class Goods:
    def __init__(self, draftorder_id=None, sale_id=None, goods_id=None, supplier_id=None, account_id= None, date= None, isfinish= None, isdelete= None):
        self.draftorder_id = draftorder_id
        self.sale_id = sale_id
        self.goods_id = goods_id
        self.supplier_id = supplier_id
        self.account_id = account_id
        self.date = date
        self.isfinish = isfinish
        self.isdelete = isdelete

if __name__ == '__main__':
    student = Goods(0,0,0,0,0,0,0,0)
    print(student.__dict__)
    for k in student.__dict__:
        print("def set_" + k + "(self," + k + "):")
        print("\tself." + k, "=" + k)
        print("def get_" + k + "(self):")
        print("\treturn self." + k)