class Goods:
    def __init__(self, goods_id=None, goods_name=None, goods_number=None, price_cost=None, price_sell=None, goods_unit=None, supplier_id=None, isdelete=None):
        self.goods_id = goods_id  # 商品编号
        self.goods_name = goods_name  # 商品名称
        self.goods_number = goods_number  # 商品库存
        self.goods_unit = goods_unit  # 商品单位
        self.price_cost = price_cost  # 商品成本
        self.price_sell = price_sell  # 商品售价
        self.supplier_id = supplier_id  # 供应商
        self.isdelete = isdelete

    def get_GoodsName(self):
        return self.goods_name

    def setGoodsName(self, goods_name):
        self.goods_name = goods_name

    def get_GoodsUnit(self):
        return self.goods_unit

    def setGoodsUnit(self, goods_unit):
        self.goods_unit = goods_unit

    def getGoods_id(self):
        return self.goods_id

    def setGoods_id(self, goods_id):
        self.goods_id = goods_id

    def getGoods_number(self):
        return self.goods_number

    def setGoods_number(self, goods_number):
        self.goods_number = goods_number

    def getPrice_cost(self):
        return self.price_cost

    def setPrice_cost(self, price_cost):
        self.price_cost = price_cost

    def getPrice_sell(self):
        return self.price_sell

    def setPrice_sell(self, price_sell):
        self.price_sell = price_sell

    def getSupplier_id(self):
        return self.supplier_id

    def setSupplier_id(self, supplier_id):
        self.supplier_id = supplier_id

    def get_isdelete(self):
        return self.isdelete

    def set_isdelete(self):
        return self.isdelete

    def getReturnTuple(self):
        return self.goods_id, self.goods_name, self.goods_number, self.price_cost, self.price_sell, self.goods_unit, self.supplier_id

