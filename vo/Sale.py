class Sale:
    def __init__(self, sale_id=None, account_id=None, customer_id=None, sale_date=None, goods_id=None, sale_number=None, sale_left=None, sale_flag=None):
        self.sale_id = sale_id  # 销售单编号
        self.account_id = account_id  # 制表人
        self.customer_id = customer_id  # 顾客编号
        self.goods_id = goods_id  # 商品编号
        self.sale_date = sale_date  # 下单时间
        self.sale_number = sale_number  # 销售数量
        self.sale_left = sale_left  # 未出库数量数量
        self.sale_flag = sale_flag  # 下单时间

    def set_sale_id(self, sale_id):
        self.sale_id = sale_id

    def get_sale_id(self):
        return self.sale_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_sale_date(self, sale_date):
        self.sale_date = sale_date

    def get_sale_date(self):
        return self.sale_date

    def set_sale_number(self, sale_number):
        self.sale_number = sale_number

    def get_sale_number(self):
        return self.sale_number

    def set_sale_left(self, sale_left):
        self.sale_left = sale_left

    def get_sale_left(self):
        return self.sale_left

    def set_sale_flag(self, sale_flag):
        self.sale_flag = sale_flag

    def get_sale_flag(self):
        return self.sale_flag

    def getReturnTuple(self):
        return self.sale_id, self.account_id, self.customer_id, self.goods_id, self.sale_date, self.sale_number, self.sale_left, self.sale_flag
