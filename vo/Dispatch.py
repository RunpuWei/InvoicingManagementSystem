class Dispatch:
    def __init__(self, dispatch_id=None, account_id=None, out_id=None, disp_date=None):
        self.dispatch_id = dispatch_id  # 发货单编号
        self.account_id = account_id  # 操作员编号
        self.out_id = out_id  # 出库单编号
        self.disp_date = disp_date  # 出库日期

    def getdispatch_id(self):
        return self.dispatch_id

    def setdispatch_id(self, dispatch_id):
        self.dispatch_id = dispatch_id

    def getaccount_id(self):
        return self.account_id

    def setaccount_id(self, account_id):
        self.account_id = account_id

    def getout_id(self):
        return self.disout_id

    def setout_id(self, out_id):
        self.out_id = out_id

    def getdisp_date(self):
        return self.disp_date

    def setdisp_date(self, disp_date):
        self.disp_date = disp_date

    def getReturnTuple(self):
        return self.dispatch_id, self.account_id, self.out_id, self.disp_date
