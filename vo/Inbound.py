class Inbound:
    def __init__(self, in_id=None, order_id=None, goods_id=None, account_id=None, in_date=None, in_num=None):
        self.in_id = in_id  # 入库单编号
        self.order_id = order_id  # 关联订货单编号
        self.goods_id = goods_id  # 商品编号
        self.account_id = account_id  # 制表人
        self.in_date = in_date  # 入库时间
        self.in_num = in_num  # 入库数量

    def getIn_num(self):
        return self.in_num

    def setIn_num(self, in_num):
        self.in_num = in_num

    def getIn_id(self):
        return self.in_id

    def setIn_id(self, in_id):
        self.in_id = in_id

    def getOrder_id(self):
        return self.order_id

    def setOrder_id(self, order_id):
        self.order_id = order_id

    def getGoods_id(self):
        return self.goods_id

    def setGoods_id(self, goods_id):
        self.goods_id = goods_id

    def getAccount_id(self):
        return self.account_id

    def setAccount_id(self, account_id):
        self.account_id = account_id

    def getIn_date(self):
        return self.in_date

    def setIn_date(self, in_date):
        self.in_date = in_date

    def getReturnTuple(self):
        return self.in_id, self.order_id, self.goods_id, self.account_id, self.in_date, self.in_num
