class Supplier:
    def __init__(self, supplier_id=None, supplier_name=None, supplier_contactor=None, supplier_phone=None, supplier_addr=None, isdelete=None):
        self.supplier_id = supplier_id  # 供应商编号
        self.supplier_name = supplier_name  # 供应商名字
        self.supplier_contactor = supplier_contactor  # 供应商联系人
        self.supplier_phone = supplier_phone  # 电话
        self.supplier_addr = supplier_addr  # 供应商地址
        self.isdelete = isdelete

    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id

    def get_supplier_id(self):
        return self.supplier_id

    def set_supplier_name(self, supplier_name):
        self.supplier_name = supplier_name

    def get_supplier_name(self):
        return self.supplier_name

    def set_supplier_contactor(self, supplier_contactor):
        self.supplier_contactor = supplier_contactor

    def get_supplier_contactor(self):
        return self.supplier_contactor

    def set_supplier_phone(self, supplier_phone):
        self.supplier_phone = supplier_phone

    def get_supplier_phone(self):
        return self.supplier_phone

    def set_supplier_addr(self, supplier_addr):
        self.supplier_addr = supplier_addr

    def get_supplier_addr(self):
        return self.supplier_addr

    def get_isdelete(self):
        return self.isdelete

    def set_isdelete(self):
        return self.isdelete


    def getReturnTuple(self):
        return self.supplier_id, self.supplier_name, self.supplier_contactor, self.supplier_phone, self.supplier_addr