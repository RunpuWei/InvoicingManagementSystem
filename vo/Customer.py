# 采购时的顾客类

class Customer:
    def __init__(self, customer_id=None, customer_name=None, customer_phone=None, customer_address=None, isdelete= None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.isdelete = isdelete

    def getCustomer_id(self):
        return self.customer_id

    def setCustomer_id(self, customer_id):
        self.customer_id = customer_id

    def getCustomer_name(self):
        return self.customer_name

    def setCustomer_name(self, customer_name):
        self.customer_name = customer_name

    def getCustomer_phone(self):
        return self.customer_phone

    def setCustomer_phone(self, customer_phone):
        self.customer_phone = customer_phone

    def getCustomer_address(self):
        return self.customer_address

    def setCustomer_id(self, customer_address):
        self.customer_address = customer_address

    def getisdelete(self):
        return self.isdelete

    def setisdelete(self, isdelete):
        self.isdelete = isdelete

    def getReturnTuple(self):
        return self.customer_id, self.customer_name, self.customer_phone, self.customer_address
