class Goods:
    def __init__(self, supplier_id, supplier_name, supplier_contactor, supplier_phone, supplier_addr):
        self.supplier_id = supplier_id  # 销售单编号
        self.supplier_name = supplier_name  # 制表人
        self.supplier_contactor = supplier_contactor  # 顾客编号
        self.supplier_phone = supplier_phone  # 商品编号
        self.supplier_addr = supplier_addr  # 下单时间

if __name__ == '__main__':
    student = Goods(0,0,0,0,0)
    print(student.__dict__)
    for k in student.__dict__:
        print("def set_" + k + "(self," + k + "):")
        print("\tself." + k, "=" + k)
        print("def get_" + k + "(self):")
        print("\treturn self." + k)