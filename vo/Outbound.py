class Outbound:
    def __init__(self, out_id=None, sale_id=None, account_id=None, out_date=None, goods_id=None, out_num=None, out_flag=None):
        self.out_id = out_id  # 出库编号
        self.sale_id = sale_id  # 关联销售单号
        self.goods_id = goods_id  # 商品编号
        self.account_id = account_id  # 管理员账号
        self.out_date = out_date  # 出库时间
        self.out_num = out_num  #
        self.out_flag = out_flag  #

    def set_out_id(self, out_id):
        self.out_id = out_id

    def get_out_id(self):
        return self.out_id

    def set_sale_id(self, sale_id):
        self.sale_id = sale_id

    def get_sale_id(self):
        return self.sale_id

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_out_date(self, out_date):
        self.out_date = out_date

    def get_out_date(self):
        return self.out_date

    def set_out_num(self, out_num):
        self.out_num = out_num

    def get_out_num(self):
        return self.out_num

    def set_out_flag(self, out_flag):
        self.out_flag = out_flag

    def get_out_flag(self):
        return self.out_flag

    def getReturnTuple(self):
        return self.out_id, self.sale_id, self.goods_id, self.account_id, self.out_date, self.out_num, self.out_flag
