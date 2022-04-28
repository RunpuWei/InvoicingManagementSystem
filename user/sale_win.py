import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QPushButton, QHBoxLayout, QTableWidgetItem, QSpinBox

from UI import user_sale
from func import SupplierFuc, ManagerFuc, GoodsFuc, SaleFuc, DispatchFuc, CustomerFuc, OutboundFuc, DraftOrderFuc
from user import widget_Goods_win as goods_win
from user import widget_Saleinfo_win as saleinfo_win
from user import widget_Customerinfo_win as customerinfo_win
from user import widget_Outboundlist as outboundlist_win
from vo.Customer import Customer
from vo.Dispatch import Dispatch
from vo.DraftOrder import DraftOrder
from vo.Manager import Manager
from vo.Sale import Sale
import sys


class InvoiceSystem(QMainWindow, user_sale.Ui_mainWindow):  # 继承自Ui_mainWindow类
    def __init__(self, mainWindow, manager=None):
        # super(InvoiceSystem, self).__init__()
        super().__init__()
        self.setupUi(mainWindow)  # 调用父类的setupUI函数
        self.statusbar.showMessage('登陆成功！', 3000)  # 信息显示3秒
        self.manager = manager
        # 设置工具栏上显示的当前用户和部门 还有 填写采购单 页面的部分空格（已完成）
        userid = self.manager.getEmployee_name()
        department = self.manager.getDepartment()
        self.Current_user.setText("当前用户：" + userid)
        self.Current_department.setText("当前部门：" + department)
        self.currentUser_sale.setText(userid)
        self.employee_name_2.setText(userid)
        self.reload()

        self.sale_goods_add.clicked.connect(self.button_addgoods)
        self.customer_add_sale.clicked.connect(self.customeradd_choose_click)
        self.sale_submit.clicked.connect(self.Sale_submit_click)
        self.submit_user_add.clicked.connect(self.customer_addCustomer)
        self.linkbutton_dispatch.clicked.connect(self.link_outbound)
        self.submit_dispatch.clicked.connect(self.submit_dispatch_clicked)
        # self.tabWidget.currentChanged.connect()
        # self.order_submit.clicked.connect(self.Order_submit_click)

    def submit_dispatch_clicked(self):
        disp_id = self.dispatch_id_dispatch.text()
        account_id = self.manager.getAccount()
        outid = self.outid.text()
        disp_date = time.strftime("%Y-%m-%d", time.localtime())

        if len(disp_id) * len(account_id) * len(outid) * len(disp_date) == 0:
            QMessageBox.warning(self, '警告', '内容没有填写完整，请填写完整后再提交！', QMessageBox.Yes)
            return None

        if OutboundFuc.updateOutboundFlagtoDelivered(self.outid.text()) and DispatchFuc.insertDispatch(
                Dispatch(disp_id, account_id, outid, disp_date)):
            QMessageBox.information(self, '提醒', '出库单' + outid + '发货成功！', QMessageBox.Yes)
            self.dispatch_id_dispatch.setText("")
            self.table_dispatch.setRowCount(0)
            dispatchlist = DispatchFuc.selectDispatch()
            self.lineEdit_18.setText(time.strftime("%Y-%m-%d", time.localtime()))
            self.dispatch_id_dispatch.setText(
                "D" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(dispatchlist) + 1))
        else:
            QMessageBox.warning(self, '提醒', '出库单' + outid + '发货失败，请联系管理员修复！', QMessageBox.Yes)

    # 当选择了关联出库单
    def link_outbound_hasChosed(self):
        source = self.sender()
        out_id = source.out_id
        out_list = OutboundFuc.selectOutboundByOutboundId(out_id)
        if out_list[0].get_out_flag() == "已发货":
            QMessageBox.warning(self, '警告', '出库单' + out_id + '已发货！', QMessageBox.Yes)
            return None
        self.dlg.close()
        self.outid.setText(out_id)
        salelist = SaleFuc.selectSaleBySaleId(out_list[0].get_sale_id())
        self.table_dispatch.setRowCount(len(out_list))
        for index, item in enumerate(out_list, 0):
            for sale in salelist:
                if sale.get_goods_id() == item.get_goods_id():
                    good = GoodsFuc.selectGoodsByGoodsId(item.get_goods_id())[0]
                    supplier = SupplierFuc.selectSupplierBySupplierId(good.getSupplier_id())[0]
                    self.table_dispatch.setItem(index, 0, QTableWidgetItem(good.getGoods_id()))  # 商品编号
                    self.table_dispatch.setItem(index, 1, QTableWidgetItem(good.get_GoodsName()))  # 商品名称
                    self.table_dispatch.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  # 商品供应商
                    self.table_dispatch.setItem(index, 3, QTableWidgetItem(str(sale.get_sale_number())))  # 售出数量
                    self.table_dispatch.setItem(index, 4, QTableWidgetItem(good.get_GoodsUnit()))  # 商品单位
                    self.table_dispatch.setItem(index, 5, QTableWidgetItem(good.getPrice_sell()))  # 商品售价
                    self.table_dispatch.setItem(index, 6, QTableWidgetItem(
                        str(sale.get_sale_number() * int(good.getPrice_sell()))))  # 商品编号
                    break

    # 发货单——关联出库单
    def link_outbound(self):
        self.dlg = outboundlist_win.win()
        outboundlist = OutboundFuc.selectOutbound()
        if outboundlist is None:
            QMessageBox.warning(self, '警告', '出库单暂时为空，请联系仓库部门！', QMessageBox.Yes)
            return
        self.dlg.table_outboundinfo.setRowCount(len(outboundlist))  # 设置表格行数

        for index, item in enumerate(outboundlist, 0):
            manager = ManagerFuc.selectManagerByAccount(item.get_account_id())[0]
            sale = SaleFuc.selectSaleBySaleId(item.get_sale_id())[0]
            customer = CustomerFuc.selectCustomerByCustomerId(sale.get_customer_id())[0]

            butinfo_temp = QPushButton("添加")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(":/img/resource/add_icon.png"))
            butinfo_temp.out_id = item.get_out_id()
            butinfo_temp.clicked.connect(self.link_outbound_hasChosed)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_outboundinfo.setItem(index, 0, QTableWidgetItem(item.get_out_id()))  # 出库单编号
            self.dlg.table_outboundinfo.setItem(index, 1, QTableWidgetItem(customer.getCustomer_name()))  # 顾客名称
            self.dlg.table_outboundinfo.setItem(index, 2, QTableWidgetItem(manager.getEmployee_name()))  # 负责人
            self.dlg.table_outboundinfo.setItem(index, 3,
                                                QTableWidgetItem(item.get_out_date().strftime('%Y-%m-%d')))  # 出库单日期
            self.dlg.table_outboundinfo.setCellWidget(index, 4, widget)  # 操作

        self.dlg.show()

    # 顾客管理——添加顾客信息
    def customer_addCustomer(self):
        id = self.customer_id_new.text()
        name = self.customer_name_new.text()
        phone = self.customer_phone_new.text()
        address = self.customer_address_new.text()
        if len(id) * len(name) * len(phone) * len(address) == 0:
            QMessageBox.warning(self, '警告', '内容没有填写完整，请填写完整后再试！', QMessageBox.Yes)
            return None
        CustomerFuc.insertCustomer(Customer(id, name, phone, address))
        QMessageBox.information(self, '提醒', '顾客' + id + '添加完成！', QMessageBox.Yes)
        self.customer_name_new.setText("")
        self.customer_phone_new.setText("")
        self.customer_address_new.setText("")

        self.user_research()
        customer_list = CustomerFuc.selectCustomer()
        self.customer_id_new.setText("C" + str(len(customer_list) + 1).rjust(4, '0'))

    # 顾客管理——顾客查询（已完成）
    def user_research(self):
        customerlist = CustomerFuc.selectCustomer()
        if customerlist is None:
            QMessageBox.warning(self, '警告', '顾客列表为空，请先添加顾客！', QMessageBox.Yes)
            return None
        for item in customerlist:
            if item.getisdelete() == 1:  #
                continue
            currentcount = self.table_user.rowCount()
            self.table_user.setRowCount(currentcount + 1)  # 设置表格行数+1

            butinfo_temp = QPushButton("删除")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/delete_icon.png'))
            butinfo_temp.customerid = item.getCustomer_id()
            butinfo_temp.clicked.connect(self.deletecustomer)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_user.setItem(currentcount, 0, QTableWidgetItem(item.getCustomer_id()))  # 顾客编号
            self.table_user.setItem(currentcount, 1, QTableWidgetItem(item.getCustomer_name()))  # 顾客姓名
            self.table_user.setItem(currentcount, 2, QTableWidgetItem(item.getCustomer_phone()))  # 顾客电话
            self.table_user.setItem(currentcount, 3, QTableWidgetItem(item.getCustomer_address()))  # 顾客地址
            self.table_user.setCellWidget(currentcount, 4, widget)  # 操作

    # 删除顾客槽函数（已做完）
    def deletecustomer(self):
        source = self.sender()
        customerid = source.customerid
        CustomerFuc.deleteCustomer(customerid)
        self.user_research()
        QMessageBox.information(QWidget(), '提醒', '顾客：' + customerid + '删除成功！', QMessageBox.Yes)

    # 销售——填写销售单 点击提交
    def Sale_submit_click(self):
        rowCount = self.table_sale.rowCount()
        if rowCount == 0:
            QMessageBox.warning(self, '警告', '你好像还没有添加商品哦！', QMessageBox.Yes)
            return None
        if len(self.order_id_sale.text()) * len(self.customer_ID_sale.text()) * len(
                self.customer_name_sale.text()) * len(self.customer_phone_sale.text()) * len(
            self.customer_address_sale.text()) * len(self.currentUser_sale.text()) * len(
            self.date_sale.text()) == 0:
            QMessageBox.warning(self, '警告', '你好像还没有选择顾客信息哦！', QMessageBox.Yes)
            return None

        saleid = self.order_id_sale.text()
        account = self.manager.getAccount()
        customerid = self.customer_ID_sale.text()
        for row in range(rowCount):
            # 自动生成暂存采购单并提交
            def DraftOrdersubmit(sale_id, goods_id, order_num, supplier_id, account_id):
                draftorderlist = DraftOrderFuc.selectDraftOrder()
                if draftorderlist is None: draftorderlist = []
                date = time.strftime("%Y-%m-%d", time.localtime())
                draftorder_id = "DB" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(draftorderlist) + 1)
                good = GoodsFuc.selectGoodsByGoodsId(goods_id)[0]
                reply = QMessageBox.question(self, '提醒', "商品\"%s\"库存不足，是否自动生成暂存订货单（订单号：\"%s\"，采购数量：\"%d\"）并提交至采购部门。" % (
                    good.get_GoodsName(), draftorder_id, order_num),
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    print('按下了确认键')
                    DraftOrderFuc.insertDraftOrder(
                        DraftOrder(draftorder_id, sale_id, goods_id, order_num, supplier_id, account_id, date))
                    return True
                else:
                    print('按下了取消键')
                    return False

            salenumber = int(int(self.table_sale.item(row, 6).text()) / int(self.table_sale.item(row, 5).text()))
            goodsid = self.table_sale.item(row, 0).text()
            goods = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]
            if salenumber > goods.getGoods_number():  # 库存不足，需要暂存采购单
                if DraftOrdersubmit(saleid, goodsid, salenumber - goods.getGoods_number(), goods.getSupplier_id(), account) is False:
                    continue

            SaleFuc.insertSale(Sale(sale_id=saleid, account_id=account, customer_id=customerid,
                                    sale_date=time.strftime("%Y-%m-%d", time.localtime()), goods_id=goodsid,
                                    sale_number=salenumber, sale_left=salenumber, sale_flag="未出库"))
        self.table_sale.setRowCount(0)  # 设置表格行数为0，清空表格

        self.saleinfo_research()
        salelist = SaleFuc.selectSale()
        if salelist is None:
            salelist = []
        self.date_sale.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.order_id_sale.setText("S" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(salelist) + 1))

        QMessageBox.information(self, '提醒', '销售单提交完成！', QMessageBox.Yes)

    # 商品管理按下添加顾客信息按钮（已完成）
    def customeradd_choose_click(self):
        # self.wid.pushButton.clicked.connect(self.GetLine)
        cuscutomerlist = CustomerFuc.selectCustomer()
        if cuscutomerlist is None:
            QMessageBox.warning(self, '警告', '顾客列表为空，请先添加顾客再试！', QMessageBox.Yes)
            return None
        self.dlg = customerinfo_win.win()
        for item in cuscutomerlist:
            if item.getisdelete() == 1:  #
                continue
            currentcount = self.dlg.table_customer.rowCount()
            self.dlg.table_customer.setRowCount(currentcount + 1)  # 设置表格行数+1

            id = item.getCustomer_id()
            name = item.getCustomer_name()
            phone = item.getCustomer_phone()
            address = item.getCustomer_address()

            supplierAddtemp = QPushButton("确定")
            supplierAddtemp.Customerid_chosed = id
            supplierAddtemp.setDown(True)
            supplierAddtemp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            supplierAddtemp.setIcon(QIcon(':/img/resource/add_icon.png'))
            supplierAddtemp.clicked.connect(self.getchosenCustomer)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(supplierAddtemp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_customer.setItem(currentcount, 0, QTableWidgetItem(id))  # 顾客编号
            self.dlg.table_customer.setItem(currentcount, 1, QTableWidgetItem(name))  # 顾客姓名
            self.dlg.table_customer.setItem(currentcount, 2, QTableWidgetItem(phone))  # 电话
            self.dlg.table_customer.setItem(currentcount, 3, QTableWidgetItem(address))  # 地址
            self.dlg.table_customer.setCellWidget(currentcount, 4, widget)  # 操作

        if self.dlg.table_customer.rowCount() == 0:
            QMessageBox.warning(self, '警告', '顾客已经全部被删除，请先添加顾客再试！', QMessageBox.Yes)
            return None
        self.dlg.show()

    # 添加顾客信息  获取选中的顾客（已完成）
    def getchosenCustomer(self):
        source = self.sender()
        cus_id = source.Customerid_chosed
        customer = CustomerFuc.selectCustomerByCustomerId(cus_id)[0]
        self.customer_ID_sale.setText(customer.getCustomer_id())
        self.customer_name_sale.setText(customer.getCustomer_name())
        self.customer_phone_sale.setText(customer.getCustomer_phone())
        self.customer_address_sale.setText(customer.getCustomer_address())
        self.dlg.close()
        print(customer)

    # 获取采购单详情（已完成）
    def SaleInfo(self):
        source = self.sender()
        sale_id = source.sale_id  # 销售单编号
        print(source)

        self.dlg = saleinfo_win.win()
        salelist = SaleFuc.selectSaleBySaleId(sale_id)  # 销售单变量
        manager = ManagerFuc.selectManagerByAccount(salelist[0].get_account_id())[0]
        customer = CustomerFuc.selectCustomerByCustomerId(salelist[0].get_customer_id())[0]

        self.dlg.sale_id.setText(sale_id)
        self.dlg.customer_id.setText(customer.getCustomer_id())
        self.dlg.customer_name.setText(customer.getCustomer_name())
        self.dlg.customer_phone.setText(customer.getCustomer_phone())
        self.dlg.customer_addr.setText(customer.getCustomer_address())
        self.dlg.sale_people.setText(manager.getEmployee_name())
        self.dlg.sale_date.setText(str(salelist[0].get_sale_date()))

        self.dlg.table_sale.setRowCount(len(salelist))  # 设置表格行数
        for index, sale in enumerate(salelist, 0):
            goods = GoodsFuc.selectGoodsByGoodsId(sale.get_goods_id())[0]
            supplier = SupplierFuc.selectSupplierBySupplierId(goods.getSupplier_id())[0]

            self.dlg.table_sale.setItem(index, 0, QTableWidgetItem(goods.getGoods_id()))  #
            self.dlg.table_sale.setItem(index, 1, QTableWidgetItem(goods.get_GoodsName()))  #
            self.dlg.table_sale.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  #
            self.dlg.table_sale.setItem(index, 3, QTableWidgetItem(str(sale.get_sale_number())))  #
            self.dlg.table_sale.setItem(index, 4, QTableWidgetItem(goods.get_GoodsUnit()))  #
            self.dlg.table_sale.setItem(index, 5, QTableWidgetItem(goods.getPrice_sell()))  #
            self.dlg.table_sale.setItem(index, 6,
                                        QTableWidgetItem(
                                            str(int(goods.getPrice_sell()) * sale.get_sale_number())))  #
            self.dlg.table_sale.setItem(index, 7, QTableWidgetItem(sale.get_sale_flag()))  #

        self.dlg.show()

    # 销售管理——销售单查询（已完成）
    def saleinfo_research(self):
        salelist = SaleFuc.selectSale()
        if salelist is None:
            salelist = []
        self.table_saleinfo.setRowCount(len(salelist))  # 设置表格行数
        for index, item in enumerate(salelist, 0):
            butinfo_temp = QPushButton("详情")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/info_icon.png'))
            butinfo_temp.sale_id = item.get_sale_id()
            butinfo_temp.clicked.connect(self.SaleInfo)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_saleinfo.setItem(index, 0, QTableWidgetItem(item.get_sale_id()))  # 销售单编号
            self.table_saleinfo.setItem(index, 1, QTableWidgetItem(
                CustomerFuc.selectCustomerByCustomerId(item.get_customer_id())[0].getCustomer_name()))  # 顾客名称
            self.table_saleinfo.setItem(index, 2, QTableWidgetItem(
                ManagerFuc.selectManagerByAccount(item.get_account_id())[0].getEmployee_name()))  # 负责人
            self.table_saleinfo.setItem(index, 3, QTableWidgetItem(item.get_sale_date().strftime('%Y-%m-%d')))  # 订单日期
            self.table_saleinfo.setCellWidget(index, 4, widget)  # 操作

    # 重新加载输入框默认值（已做完）
    def reload(self):
        self.table_saleinfo.setRowCount(0)
        self.table_user.setRowCount(0)

        self.user_research()
        self.saleinfo_research()

        salelist = SaleFuc.selectSale()
        self.date_sale.setText(time.strftime("%Y-%m-%d", time.localtime()))
        if salelist is None:
            self.order_id_sale.setText("S" + str(int(time.strftime("%Y%m0000", time.localtime())) + 1))
        else:
            self.order_id_sale.setText("S" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(salelist) + 1))

        dispatchlist = DispatchFuc.selectDispatch()
        self.lineEdit_18.setText(time.strftime("%Y-%m-%d", time.localtime()))
        if dispatchlist is None:
            self.dispatch_id_dispatch.setText(
                "D" + str(int(time.strftime("%Y%m0000", time.localtime())) + 1))
        else:
            self.dispatch_id_dispatch.setText(
                "D" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(dispatchlist) + 1))

        customer_list = CustomerFuc.selectCustomer()
        if customer_list is None:
            self.customer_id_new.setText("C" + str(1).rjust(4, '0'))
        else:
            self.customer_id_new.setText("C" + str(len(customer_list) + 1).rjust(4, '0'))

    # 销售——添加商品按钮（已做完）
    def button_addgoods(self):
        self.dlg = goods_win.win()
        goods = GoodsFuc.selectGoods()
        good_num = len(goods)
        for good in goods:
            if good.get_isdelete() == 1:  #
                continue
            currentcount = self.dlg.table_goods.rowCount()
            self.dlg.table_goods.setRowCount(currentcount + 1)  # 设置表格行数+1
            butadd = QPushButton("添加")
            butadd.setDown(True)
            butadd.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butadd.setIcon(QIcon(':/img/resource/add_icon.png'))
            butadd.goodsid = good.getGoods_id()
            butadd.clicked.connect(self.sale_addgoods)
            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butadd)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_goods.setItem(currentcount, 0, QTableWidgetItem(good.getGoods_id()))  #
            self.dlg.table_goods.setItem(currentcount, 1, QTableWidgetItem(good.get_GoodsName()))  #
            self.dlg.table_goods.setItem(currentcount, 2, QTableWidgetItem(good.get_GoodsUnit()))  #
            self.dlg.table_goods.setItem(currentcount, 3, QTableWidgetItem(good.getSupplier_id()))  #
            self.dlg.table_goods.setItem(currentcount, 4, QTableWidgetItem(good.getPrice_sell()))  #
            self.dlg.table_goods.setItem(currentcount, 5, QTableWidgetItem(str(good.getGoods_number())))  #
            self.dlg.table_goods.setItem(currentcount, 6, QTableWidgetItem(good.getPrice_cost()))  #
            self.dlg.table_goods.setCellWidget(currentcount, 7, widget)  #

        self.dlg.show()

    # 销售单添加商品——槽函数（已做完）
    def sale_addgoods(self):
        source = self.sender()
        goodsid = source.goodsid  # 商品编号
        good = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]

        for row in range(self.table_sale.rowCount()):
            if self.table_sale.item(row, 0).text() == goodsid:
                QMessageBox.warning(QWidget(), '警告', '列表内已含有该商品！', QMessageBox.Yes)
                return None

        cur_row_count = self.table_sale.rowCount()  # 当前行数
        cur_row_count += 1
        self.table_sale.setRowCount(cur_row_count)

        # 创建删除按钮
        butdelete = QPushButton("删除")
        butdelete.setDown(True)
        butdelete.setStyleSheet(''' text-align : center;
                                          border: 2px solid #e7e7e7;
                                          height : 30px;
                                          border-top:1px solid #eee;
                                          font : 13px;''')
        butdelete.setIcon(QIcon(':/img/resource/delete_icon.png'))
        butdelete.goodsid = goodsid
        butdelete.clicked.connect(self.sale_deletegoods)
        widget = QWidget()
        hLayout = QHBoxLayout()
        hLayout.addWidget(butdelete)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        # 创建spinBox
        spinBox = QSpinBox()
        spinBox.setRange(1, 999999)
        spinBox.setSingleStep(1)
        spinBox.valueChanged.connect(self.sale_setgoodsnum)
        spinBox.goodsid = goodsid

        editwidget = QWidget()
        edithLayout = QHBoxLayout()
        edithLayout.addWidget(spinBox)
        edithLayout.setContentsMargins(5, 2, 5, 2)
        editwidget.setLayout(edithLayout)

        self.table_sale.setItem(cur_row_count - 1, 0, QTableWidgetItem(good.getGoods_id()))  #
        self.table_sale.setItem(cur_row_count - 1, 1, QTableWidgetItem(good.get_GoodsName()))  #
        self.table_sale.setItem(cur_row_count - 1, 2, QTableWidgetItem(good.getSupplier_id()))  #
        self.table_sale.setCellWidget(cur_row_count - 1, 3, editwidget)  # 销售数量（编辑框）
        self.table_sale.setItem(cur_row_count - 1, 4, QTableWidgetItem(good.get_GoodsUnit()))  #
        self.table_sale.setItem(cur_row_count - 1, 5, QTableWidgetItem(good.getPrice_sell()))  # 单价
        self.table_sale.setItem(cur_row_count - 1, 6, QTableWidgetItem(good.getPrice_sell()))  # 总金额
        self.table_sale.setCellWidget(cur_row_count - 1, 7, widget)  # 删除按钮

        QMessageBox.information(self, '提醒', '商品\"' + good.get_GoodsName() + "\"添加成功！", QMessageBox.Yes)

    # 销售——修改商品数量（已做完）
    def sale_setgoodsnum(self):
        source = self.sender()
        if source:
            goods = GoodsFuc.selectGoodsByGoodsId(source.goodsid)[0]
            for row in range(self.table_sale.rowCount()):
                if self.table_sale.item(row, 0).text() == goods.getGoods_id():
                    num = source.value()
                    if num > goods.getGoods_number():
                        QMessageBox.information(self, '提醒',
                                                "您设置的销售数量(%s%s)超过了商品\"%s\"当前的库存数量(%s%s)，如果继续销售则系统会自动生成暂存订货单提交至采购部门。" % (
                                                    num, goods.get_GoodsUnit(), goods.get_GoodsName(),
                                                    goods.getGoods_number(), goods.get_GoodsUnit()),
                                                QMessageBox.Yes)
                    sell = int(self.table_sale.item(row, 5).text())
                    self.table_sale.setItem(row, 6, QTableWidgetItem(str(num * sell)))  #
                    break

    # 销售管理——删除商品（已做完）
    def sale_deletegoods(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            for row in range(self.table_sale.rowCount()):
                if self.table_sale.item(row, 0).text() == goodsid:
                    self.table_sale.removeRow(row)
                    break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InvoiceSystem(MainWindow, Manager(2, 2, "销售员", "销售部门"))  # 注意把类名修改为myDialog
    # ui.setupUi(MainWindow)  myDialog类的构造函数已经调用了这个函数，这行代码可以删去
    MainWindow.show()
    sys.exit(app.exec_())
