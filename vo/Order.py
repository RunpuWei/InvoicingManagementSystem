class Order:
    def __init__(self, order_id=None, account_id=None, supplier_id=None, order_date=None, pur_id=None, goods_id=None, order_flag=None,
                 order_number=None,
                 order_left=None):
        self.order_id = order_id  # 订货单编号
        self.account_id = account_id  # 管理员编号
        self.supplier_id = supplier_id  # 供应商编号
        self.pur_id = pur_id  # 关联采购申请单数量
        self.order_date = order_date  # 采购时间
        self.goods_id = goods_id  # 商品编号
        self.order_flag = order_flag  #
        self.order_number = order_number  #
        self.order_left = order_left  #

    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_order_id(self):
        return self.order_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id

    def get_supplier_id(self):
        return self.supplier_id

    def set_pur_id(self, pur_id):
        self.pur_id = pur_id

    def get_pur_id(self):
        return self.pur_id

    def set_order_date(self, order_date):
        self.order_date = order_date

    def get_order_date(self):
        return self.order_date

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_order_flag(self, order_flag):
        self.order_flag = order_flag

    def get_order_flag(self):
        return self.order_flag

    def set_order_number(self, order_number):
        self.order_number = order_number

    def get_order_number(self):
        return self.order_number

    def set_order_left(self, order_left):
        self.order_left = order_left

    def get_order_left(self):
        return self.order_left

    def getReturnTuple(self):
        return self.order_id, self.account_id, self.supplier_id, self.order_left, \
               self.order_date, self.goods_id, self.order_flag, self.order_number
