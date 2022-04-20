class Purchase:
    def __init__(self, pur_id, account_id, sale_id, goods_id, pur_date, pur_number):
        self.pur_id = pur_id  # 销售单编号
        self.account_id = account_id  # 制表人
        self.sale_id = sale_id  # 顾客编号
        self.goods_id = goods_id # 商品编号
        self.pur_date = pur_date  # 下单时间
        self.pur_number = pur_number  # 销售数量

    def set_pur_id(self, pur_id):
        self.pur_id = pur_id

    def get_pur_id(self):
        return self.pur_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_sale_id(self, sale_id):
        self.sale_id = sale_id

    def get_sale_id(self):
        return self.sale_id

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_pur_date(self, pur_date):
        self.pur_date = pur_date

    def get_pur_date(self):
        return self.pur_date

    def set_pur_number(self, pur_number):
        self.pur_number = pur_number

    def get_pur_number(self):
        return self.pur_number

    def getReturnTuple(self):
        return self.pur_id, self.account_id, self.sale_id, self.goods_id, self.pur_date, self.pur_number
