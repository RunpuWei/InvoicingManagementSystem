class Return:
    def __init__(self, re_id=None, account_id=None, order_id=None, re_date=None, goods_id=None):
        self.re_id = re_id  # 销售单编号
        self.account_id = account_id  # 制表人
        self.order_id = order_id  # 顾客编号
        self.goods_id = goods_id  # 商品编号
        self.re_date = re_date  # 下单时间

    def set_re_id(self, re_id):
        self.re_id = re_id

    def get_re_id(self):
        return self.re_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_order_id(self):
        return self.order_id

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_re_date(self, re_date):
        self.re_date = re_date

    def get_re_date(self):
        return self.re_date

    def getReturnTuple(self):
        return self.re_id, self.account_id, self.order_id, self.goods_id, self.re_date