class Manager:
    def __init__(self, account=None, password=None, employee_name=None, department=None):
        self.account = account  # 账号
        self.password = password  # 面面
        self.department = department  # 部门
        self.employee_name = employee_name  # 名字

    def getAccount(self):
        return self.account

    def setAccount(self, account):
        self.account = account

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getEmployee_name(self):
        return self.employee_name

    def setEmployee_name(self, employee_name):
        self.employee_name = employee_name

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department

