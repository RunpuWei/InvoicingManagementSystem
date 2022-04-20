import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton, QHBoxLayout, QTableWidgetItem

from func import OrderFuc, SupplierFuc, ManagerFuc


# 退出按钮动作
def act_exit(self):
    w = QWidget()  # 没有父类的widget将被作为窗口使用
    # 退出确定框
    reply = QMessageBox.question(w, '退出', '确定退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        print('退出')
        sys.exit()
    else:
        print('不退出')


# 采购管理——填写采购单
def act_order_submit_clicked(self):
    orderid = self.order_id_order_2.text()
    order_date = self.order_date.text()
    print(orderid)
    print(order_date)


# 采购管理——采购单查询
def getTable_OrderInfo_data(self):
    orderinfo = OrderFuc.selectOrder()
    self.table_orderinfo.setRowCount(len(orderinfo))  # 设置表格行数
    self.table_orderinfo.horizontalHeader().setStyleSheet("""QHeaderView::section {background-color:#008CBA ; /* 蓝色 */
                                                            color: WHITE;
                                                            };
                                                            text-align : center;""")
    self.but_info = []
    for index, item in enumerate(orderinfo, 0):
        supplier_id = item.get_supplier_id()
        account_id = item.get_account_id()

        supplier = SupplierFuc.selectSupplierBySupplierId(supplier_id)
        manage = ManagerFuc.selectManagerByAccount(account_id)

        but_info_temp = QPushButton("详情")
        but_info_temp.setDown(True)
        but_info_temp.setStyleSheet(''' text-align : center;
                                          border: 2px solid #e7e7e7;
                                          height : 30px;
                                          border-top:1px solid #eee;
                                          font : 13px;''')
        but_info_temp.setIcon(QIcon('../resource/info_icon.png'))
        but_info_temp.clicked.connect(lambda: print("触发了按钮单击，点击的按钮是："+str(but_info_temp))) # 这里还没写好，因为还没画采购单详情界面！！

        widget = QWidget()
        hLayout = QHBoxLayout()
        hLayout.addWidget(but_info_temp)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        self.table_orderinfo.setItem(index, 0, QTableWidgetItem(item.get_order_id()))  # 供应商编号
        self.table_orderinfo.setItem(index, 1, QTableWidgetItem(supplier[0].get_supplier_name()))  # 供应商名称
        self.table_orderinfo.setItem(index, 2, QTableWidgetItem(manage[0].getEmployee_name()))  # 负责人
        self.table_orderinfo.setItem(index, 3, QTableWidgetItem(item.get_order_date().strftime('%Y-%m-%d')))  # 订单日期
        self.table_orderinfo.setCellWidget(index, 4, widget)  # 操作

    print(orderinfo)


def act_order_goods_add(self):
    global purchasing_goods  # 储存采购单内的商品
    self.tabWidget.setCurrentIndex(2)
    self.Box_goods.setCurrentIndex(0)


# 列表内添加按钮
def buttonForOrder(self, id):
    widget = QWidget()
    # 修改
    updateBtn = QPushButton('修改')
    updateBtn.setStyleSheet(''' text-align : center;
                                      background-color : NavajoWhite;
                                      height : 30px;
                                      border-style: outset;
                                      font : 13px  ''')

    updateBtn.clicked.connect(lambda: self.updateTable(id))

    # 查看
    viewBtn = QPushButton('查看')
    viewBtn.setStyleSheet(''' text-align : center;
                              background-color : DarkSeaGreen;
                              height : 30px;
                              border-style: outset;
                              font : 13px; ''')

    viewBtn.clicked.connect(lambda: self.viewTable(id))

    # 删除
    deleteBtn = QPushButton('删除')
    deleteBtn.setStyleSheet(''' text-align : center;
                                background-color : LightCoral;
                                height : 30px;
                                border-style: outset;
                                font : 13px; ''')

    hLayout = QHBoxLayout()
    hLayout.addWidget(updateBtn)
    hLayout.addWidget(viewBtn)
    hLayout.addWidget(deleteBtn)
    hLayout.setContentsMargins(5, 2, 5, 2)
    widget.setLayout(hLayout)
    return widget
