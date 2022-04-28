# 暂存订货单类

class DraftOrder:
    def __init__(self, draftorder_id=None, sale_id=None, goods_id=None, order_num=None, supplier_id=None, account_id=None, date=None,
                 isfinish=None, isdelete=None):
        self.draftorder_id = draftorder_id
        self.sale_id = sale_id
        self.goods_id = goods_id
        self.order_num = order_num
        self.supplier_id = supplier_id
        self.account_id = account_id
        self.date = date
        self.isfinish = isfinish
        self.isdelete = isdelete

    def set_draftorder_id(self, draftorder_id):
        self.draftorder_id = draftorder_id

    def get_draftorder_id(self):
        return self.draftorder_id

    def set_sale_id(self, sale_id):
        self.sale_id = sale_id

    def get_sale_id(self):
        return self.sale_id

    def set_goods_id(self, goods_id):
        self.goods_id = goods_id

    def get_goods_id(self):
        return self.goods_id

    def set_order_num(self, order_num):
        self.order_num = order_num

    def get_order_num(self):
        return self.order_num

    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id

    def get_supplier_id(self):
        return self.supplier_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_isfinish(self, isfinish):
        self.isfinish = isfinish

    def get_isfinish(self):
        return self.isfinish

    def set_isdelete(self, isdelete):
        self.isdelete = isdelete

    def get_isdelete(self):
        return self.isdelete

    def getReturnTuple(self):
        return self.draftorder_id, self.sale_id, self.goods_id, self.order_num, self.supplier_id, self.account_id, self.date, self.isfinish, self.isdelete
