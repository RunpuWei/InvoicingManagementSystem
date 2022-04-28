import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QPushButton, QHBoxLayout, QTableWidgetItem, QSpinBox

from UI import user_purchasing
from func import OrderFuc, SupplierFuc, ManagerFuc, GoodsFuc, ReturnFuc, DraftOrderFuc
from user import widget_Supplier_win as supplier_win
from user import widget_Orderinfo_win as orderinfo_win
from user import widget_Goods_win as goods_win
from user import widget_Purchaseorderquery_win as purchaseorderquery_win
from vo.Goods import Goods
from vo.Manager import Manager
from vo.Return import Return
from vo.Order import Order
from vo.Supplier import Supplier
import sys


class InvoiceSystem(QMainWindow, user_purchasing.Ui_mainWindow):  # 继承自Ui_mainWindow类

    def __init__(self, mainWindow, manager=None):
        super().__init__()
        self.setupUi(mainWindow)  # 调用父类的setupUI函数
        self.setFixedSize(self.width(), self.height())
        self.statusbar.showMessage('登陆成功！', 3000)  # 信息显示3秒
        self.manager = manager
        self.setToolbarUserinfo()
        self.reload()
        # self.tabWidget.currentChanged.connect()
        self.order_submit.clicked.connect(self.Order_submit_click)
        self.Box_purchasing.currentChanged.connect(self.Box_purchasing_changed)
        self.supplier_add.clicked.connect(self.supplier_add_click)
        self.order_goods_add.clicked.connect(self.purchase_addgoods)
        self.linkbutton_return.clicked.connect(self.linkorder_return)
        self.return_button.clicked.connect(self.return_button_click)
        self.ChooseSupplier_goods_add.clicked.connect(self.supplier_choose_click)
        self.submit_goods_add.clicked.connect(self.goods_addGood)
        self.submit_supplier_add.clicked.connect(self.supplier_addSupplier)

    # 供应商管理——添加供应商信息
    def supplier_addSupplier(self):
        id = self.supplierid_supplier_add.text()
        name = self.name_supplier_add.text()
        contact = self.contact_supplier_add.text()
        tel = self.tel_supplier_add.text()
        add = self.address_supplier_add.text()  # 单位成本
        if len(id) * len(name) * len(contact) * len(tel) * len(add) == 0:
            QMessageBox.warning(self, '警告', '内容没有填写完整，请填写完整后再试！', QMessageBox.Yes)
            return None
        SupplierFuc.insertSupplier(Supplier(id, name, contact, tel, add))
        QMessageBox.information(self, '提醒', '供应商' + id + '添加完成！', QMessageBox.Yes)

        self.name_supplier_add.setText("")
        self.contact_supplier_add.setText("")
        self.tel_supplier_add.setText("")
        self.address_supplier_add.setText("")

        self.table_supplier.setRowCount(0)
        self.supplier_research()
        supplier_list = SupplierFuc.selectSupplier()
        newsupplierid = "G" + str(len(supplier_list) + 1).rjust(4, '0')
        self.supplierid_supplier_add.setText(newsupplierid)

    # 一级页面切换（弃用）
    def tabchange(self):
        index = self.tabWidget.currentIndex()

    # 采购管理——暂存采购单查询
    def draftOrder_research(self):
        draftorder_list = DraftOrderFuc.selectDraftOrder()
        for item in draftorder_list:
            if item.get_isdelete() == 1 or item.get_isfinish() == 1:  #
                continue
            currentcount = self.table_draftOrder.rowCount()
            self.table_draftOrder.setRowCount(currentcount + 1)  # 设置表格行数+1

            butinfo_addtemp = QPushButton("接受")
            butinfo_addtemp.setDown(True)
            butinfo_addtemp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_addtemp.setIcon(QIcon(':/img/resource/add_icon.png'))
            butinfo_addtemp.draftorder_id = item.get_draftorder_id()
            butinfo_addtemp.clicked.connect(self.draftOrder_setfinished)

            butinfo_deletetemp = QPushButton("拒绝")
            butinfo_deletetemp.setDown(True)
            butinfo_deletetemp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_deletetemp.setIcon(QIcon(':/img/resource/delete_icon.png'))
            butinfo_deletetemp.draftorder_id = item.get_draftorder_id()
            butinfo_deletetemp.clicked.connect(self.draftOrder_setdelete)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_addtemp)
            hLayout.addWidget(butinfo_deletetemp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            goods = GoodsFuc.selectGoodsByGoodsId(item.get_goods_id())[0]
            supplier = SupplierFuc.selectSupplierBySupplierId(item.get_supplier_id())[0]
            manager = ManagerFuc.selectManagerByAccount(item.get_account_id())[0]

            self.table_draftOrder.setItem(currentcount, 0, QTableWidgetItem(item.get_draftorder_id()))  # 暂存订货单编号
            self.table_draftOrder.setItem(currentcount, 1, QTableWidgetItem(item.get_sale_id()))  # 关联销售单编号
            self.table_draftOrder.setItem(currentcount, 2, QTableWidgetItem(
                "%s/%s" % (goods.get_GoodsName(), goods.getGoods_id())))  # 商品名/商品ID
            self.table_draftOrder.setItem(currentcount, 3, QTableWidgetItem(str(item.get_order_num())+goods.get_GoodsUnit()))  # 订货数量
            self.table_draftOrder.setItem(currentcount, 4, QTableWidgetItem(
                "%s/%s" % (supplier.get_supplier_name(), supplier.get_supplier_id())))  # 供应商名/供应商ID
            self.table_draftOrder.setItem(currentcount, 5, QTableWidgetItem(manager.getEmployee_name()))  # 负责人
            self.table_draftOrder.setItem(currentcount, 6,
                                          QTableWidgetItem(item.get_date().strftime('%Y-%m-%d')))  # 库存数量
            self.table_draftOrder.setCellWidget(currentcount, 7, widget)  # 操作

    # 采购管理——删除暂存采购单
    def draftOrder_setdelete(self):
        source = self.sender()
        if source:
            draftorder_id = source.draftorder_id
            for row in range(self.table_draftOrder.rowCount()):
                if self.table_draftOrder.item(row, 0).text() == draftorder_id:
                    DraftOrderFuc.deletedraftorder(draftorder_id)
                    self.table_draftOrder.removeRow(row)
                    QMessageBox.information(self, '提醒', '暂存采购单' + draftorder_id + '拒绝成功！', QMessageBox.Yes)
                    break

    # 采购管理——完成暂存采购单
    def draftOrder_setfinished(self):
        source = self.sender()
        if source:
            draftorder_id = source.draftorder_id
            for row in range(self.table_draftOrder.rowCount()):
                if self.table_draftOrder.item(row, 0).text() == draftorder_id:
                    DraftOrderFuc.setDraftOrderfinished(draftorder_id)
                    self.table_draftOrder.removeRow(row)
                    QMessageBox.information(self, '提醒', '暂存采购单' + draftorder_id + '接受成功！', QMessageBox.Yes)
                    break

    # 商品管理按下选择供应商按钮（已完成）
    def supplier_choose_click(self):
        supplierinfo = SupplierFuc.selectSupplier()
        if supplierinfo is None:
            QMessageBox.warning(self, '警告', '暂无供应商，请先添加供应商！', QMessageBox.Yes)
            return None
        self.dlg = supplier_win.win()
        self.dlg.table_supplier.horizontalHeader().setStyleSheet("""QHeaderView::section {background-color:#008CBA ; /* 蓝色 */
                                                                color: WHITE;
                                                                };
                                                                text-align : center;""")
        for item in supplierinfo:
            if item.get_isdelete() == 1:  #
                continue
            currentcount = self.dlg.table_supplier.rowCount()
            self.dlg.table_supplier.setRowCount(currentcount + 1)  # 设置表格行数+1

            id = item.get_supplier_id()
            name = item.get_supplier_name()
            contactor = item.get_supplier_contactor()
            phone = item.get_supplier_phone()
            add = item.get_supplier_addr()

            supplierAddtemp = QPushButton("确定")
            supplierAddtemp.SupplierId_Chosed = id
            supplierAddtemp.setDown(True)
            supplierAddtemp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            supplierAddtemp.setIcon(QIcon(':/img/resource/add_icon.png'))
            supplierAddtemp.clicked.connect(self.getchosenSupplier_goodAdd)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(supplierAddtemp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_supplier.setItem(currentcount, 0, QTableWidgetItem(id))  # 供应商编号
            self.dlg.table_supplier.setItem(currentcount, 1, QTableWidgetItem(name))  # 供应商名称
            self.dlg.table_supplier.setItem(currentcount, 2, QTableWidgetItem(contactor))  # 负责人
            self.dlg.table_supplier.setItem(currentcount, 3, QTableWidgetItem(phone))  # 联系人电话
            self.dlg.table_supplier.setItem(currentcount, 4, QTableWidgetItem(add))  # 供应商地址
            self.dlg.table_supplier.setCellWidget(currentcount, 5, widget)  # 操作

        if self.dlg.table_supplier.rowCount() == 0:
            QMessageBox.warning(self, '警告', '暂无可以显示的供应商，请检查供应商是否均已删除！', QMessageBox.Yes)
            return None
        self.dlg.show()

    # 添加供应商 获取选中的供应商（已完成）
    def getchosenSupplier_goodAdd(self):
        source = self.sender()
        Supplier_id = source.SupplierId_Chosed
        self.supplier_goods_add.setText(Supplier_id)
        self.dlg.close()
        print(Supplier_id)

    # 供应商管理——供应商查询（已做完）
    def supplier_research(self):
        supplier_list = SupplierFuc.selectSupplier()
        for index, item in enumerate(supplier_list, 0):
            if item.get_isdelete() == 1:  #
                continue
            currentcount = self.table_supplier.rowCount()
            self.table_supplier.setRowCount(currentcount + 1)  # 设置表格行数+1

            butinfo_temp = QPushButton("删除")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/delete_icon.png'))
            butinfo_temp.supplierid = item.get_supplier_id()
            butinfo_temp.clicked.connect(self.deleteSupplier)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_supplier.setItem(currentcount, 0, QTableWidgetItem(item.get_supplier_id()))  # 供应商编号
            self.table_supplier.setItem(currentcount, 1, QTableWidgetItem(item.get_supplier_name()))  # 名称
            self.table_supplier.setItem(currentcount, 2, QTableWidgetItem(item.get_supplier_contactor()))  # 联系人
            self.table_supplier.setItem(currentcount, 3, QTableWidgetItem(item.get_supplier_phone()))  # 电话
            self.table_supplier.setItem(currentcount, 4, QTableWidgetItem(item.get_supplier_addr()))  # 地址
            self.table_supplier.setCellWidget(currentcount, 5, widget)  # 操作

    # 删除供应商槽函数（已做完）
    def deleteSupplier(self):
        source = self.sender()
        supplierid = source.supplierid
        SupplierFuc.deleteSupplier(supplierid)
        self.table_supplier.setRowCount(0)
        self.supplier_research()
        QMessageBox.information(self, '提醒', '供应商ID：' + supplierid + '删除成功！', QMessageBox.Yes)

    # 商品管理——添加商品信息
    def goods_addGood(self):
        goodid = self.goodsid_goods_add.text()
        goodsname = self.goodsname_goods_add.text()
        goodnumber = self.stock_goods_add.text()
        goodunit = self.unit_goods_add.text()
        goodunitcost = self.unitcost_goods_add.text()  # 单位成本
        goodprice = self.price_goods_add.text()  # 零售价
        supplierid = self.supplier_goods_add.text()
        if len(goodid) * len(goodsname) * len(goodnumber) * len(goodunit) * len(goodunitcost) * len(goodprice) * len(
                supplierid) == 0:
            QMessageBox.warning(self, '警告', '内容没有填写完整，请填写完整后再试！', QMessageBox.Yes)
            return None
        GoodsFuc.insertGoods(Goods(goodid, goodsname, goodnumber, goodunitcost, goodprice, goodunit, supplierid))

        self.table_goods.setRowCount(0)
        self.goods_research()
        goods_list = GoodsFuc.selectGoods()
        newgoodsid = "P" + str(len(goods_list) + 1).rjust(4, '0')
        self.goodsid_goods_add.setText(newgoodsid)

        QMessageBox.information(self, '提醒', '商品' + goodid + '添加完成！', QMessageBox.Yes)

    # 商品管理——商品查询（已做完）
    def goods_research(self):
        goods_list = GoodsFuc.selectGoods()
        for item in goods_list:
            if item.get_isdelete() == 1:  #
                continue
            currentcount = self.table_goods.rowCount()
            self.table_goods.setRowCount(currentcount + 1)  # 设置表格行数+1
            butinfo_temp = QPushButton("删除")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/delete_icon.png'))
            butinfo_temp.goodsid = item.getGoods_id()
            butinfo_temp.clicked.connect(self.deleteGoods)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_goods.setItem(currentcount, 0, QTableWidgetItem(item.getGoods_id()))  # 商品编号
            self.table_goods.setItem(currentcount, 1, QTableWidgetItem(item.get_GoodsName()))  # 商品名称
            self.table_goods.setItem(currentcount, 2, QTableWidgetItem(item.get_GoodsUnit()))  # 商品单位
            self.table_goods.setItem(currentcount, 3, QTableWidgetItem(item.getSupplier_id()))  # 供应商
            self.table_goods.setItem(currentcount, 4, QTableWidgetItem(item.getPrice_sell()))  # 销售单价
            self.table_goods.setItem(currentcount, 5, QTableWidgetItem(str(item.getGoods_number())))  # 库存数量
            self.table_goods.setItem(currentcount, 6, QTableWidgetItem(item.getPrice_cost()))  # 成本单价
            self.table_goods.setCellWidget(currentcount, 7, widget)  # 操作

    # 删除商品槽函数（已做完）
    def deleteGoods(self):
        source = self.sender()
        goodsid = source.goodsid
        GoodsFuc.deleteGoods(goodsid)
        self.table_goods.setRowCount(0)
        self.goods_research()
        QMessageBox.information(self, '提醒', '商品ID：' + goodsid + '删除成功！', QMessageBox.Yes)

    # 退货——添加 点击提交（已做完）
    def return_button_click(self):
        rowCount = self.table_return.rowCount()
        if rowCount == 0:
            QMessageBox.warning(self, '警告', '退货单为空，请重新选择采购单再试！', QMessageBox.Yes)
            return None
        order_id = self.order_id_2.text()
        order = OrderFuc.selectOrderByOrderId(order_id)[0]
        return_date = self.lineEdit_18.text()
        user_id = self.manager.getAccount()
        re_id = self.return_id_return.text()
        for row in range(rowCount):
            goodsid = self.table_return.item(row, 0).text()
            ReturnFuc.insertReturn(
                Return(re_id=re_id, account_id=user_id, order_id=order_id, re_date=return_date, goods_id=goodsid))
            OrderFuc.updateOrderFlag(Order(order_left=0, order_id=order_id, goods_id=goodsid, order_flag="已退货"))

        self.table_return.setRowCount(0)  # 设置表格行数为0，清空表格
        returnList = ReturnFuc.selectReturn()
        self.lineEdit_18.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.return_id_return.setText("R" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(returnList) + 1))

        QMessageBox.information(self, '提醒', '退货单提交完成！', QMessageBox.Yes)

    # 填写退货单——关联采购单按钮（已完成）
    def linkorder_return(self):
        self.dlg = purchaseorderquery_win.win()

        orderinfo = OrderFuc.selectOrder()
        self.dlg.table_orderinfo.setRowCount(len(orderinfo))  # 设置表格行数

        for index, item in enumerate(orderinfo, 0):
            supplier_id = item.get_supplier_id()
            account_id = item.get_account_id()

            supplier = SupplierFuc.selectSupplierBySupplierId(supplier_id)
            manage = ManagerFuc.selectManagerByAccount(account_id)

            butinfo_temp = QPushButton("添加")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/add_icon.png'))
            butinfo_temp.order_id = item.get_order_id()
            butinfo_temp.clicked.connect(self.writeOrderid)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_orderinfo.setItem(index, 0, QTableWidgetItem(item.get_order_id()))  # 采购单编号
            self.dlg.table_orderinfo.setItem(index, 1, QTableWidgetItem(supplier[0].get_supplier_name()))  # 供应商名称
            self.dlg.table_orderinfo.setItem(index, 2, QTableWidgetItem(manage[0].getEmployee_name()))  # 负责人
            self.dlg.table_orderinfo.setItem(index, 3,
                                             QTableWidgetItem(item.get_order_date().strftime('%Y-%m-%d')))  # 订单日期

            self.dlg.table_orderinfo.setCellWidget(index, 4, widget)  # 操作

        self.dlg.show()

    # 退货管理——获取并写入关联采购单槽函数
    def writeOrderid(self):
        source = self.sender()
        orderlist = OrderFuc.selectOrderByOrderId(source.order_id)
        for i in orderlist:
            if i.get_order_flag() != "未入库":
                QMessageBox.warning(self, '警告', '该订单已入库，无法退货！', QMessageBox.Yes)
                return None
        self.order_id_2.setText(source.order_id)  # 填入关联订货单编号栏
        self.dlg.close()
        self.table_return.setRowCount(len(orderlist))  # 设置表格行数

        for index, item in enumerate(orderlist, 0):
            goods_id = item.get_goods_id()
            goods = GoodsFuc.selectGoodsByGoodsId(goods_id)[0]
            supplier_id = item.get_supplier_id()
            supplier = \
                SupplierFuc.selectSupplierBySupplierId(GoodsFuc.selectGoodsByGoodsId(goods_id)[0].getSupplier_id())[0]
            order_id = item.get_order_id()
            order = OrderFuc.selectOrderByOrderId(order_id)[0]

            account_id = item.get_account_id()
            order_date = item.get_order_date()

            butinfo_temp = QPushButton("删除")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/delete_icon.png'))

            butinfo_temp.goods_id = item.get_goods_id()  # 把商品编号赋值给按钮
            butinfo_temp.clicked.connect(self.return_deletegoods)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_return.setItem(index, 0, QTableWidgetItem(goods_id))  # 商品编号
            self.table_return.setItem(index, 1, QTableWidgetItem(goods.get_GoodsName()))  # 商品名称
            self.table_return.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  # 商品供应商
            self.table_return.setItem(index, 3, QTableWidgetItem(str(item.get_order_number())))  # 发货数量
            self.table_return.setItem(index, 4, QTableWidgetItem(goods.get_GoodsUnit()))  # 商品单位
            self.table_return.setItem(index, 5, QTableWidgetItem(goods.getPrice_cost()))  # 单价
            self.table_return.setItem(index, 6,
                                      QTableWidgetItem(str(item.get_order_number() * int(goods.getPrice_cost()))))  # 金额
            self.table_return.setCellWidget(index, 7, widget)  # 操作

    # 退货——删除采购商品（已做完）
    def return_deletegoods(self):
        source = self.sender()
        if source:
            goodsid = source.goods_id
            for row in range(self.table_return.rowCount()):
                if self.table_return.item(row, 0).text() == goodsid:
                    self.table_return.removeRow(row)
                    break

    # 重新加载输入框默认值（已做完）
    def reload(self):
        self.table_order.setRowCount(0)
        self.table_orderinfo.setRowCount(0)
        self.table_return.setRowCount(0)
        self.table_goods.setRowCount(0)
        self.table_supplier.setRowCount(0)

        self.goods_research()
        self.supplier_research()

        orderlist = OrderFuc.selectOrder()
        if orderlist is None: orderlist = []
        self.order_date.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.order_id_order_2.setText("B" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(orderlist) + 1))

        returnList = ReturnFuc.selectReturn()
        if returnList is None: returnList = []
        self.lineEdit_18.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.return_id_return.setText("R" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(returnList) + 1))

        goods_list = GoodsFuc.selectGoods()
        if goods_list is None: goods_list = []
        newgoodsid = "P" + str(len(goods_list) + 1).rjust(4, '0')
        self.goodsid_goods_add.setText(newgoodsid)

        supplier_list = SupplierFuc.selectSupplier()
        if supplier_list is None: supplier_list = []
        newsupplierid = "G" + str(len(supplier_list) + 1).rjust(4, '0')
        self.supplierid_supplier_add.setText(newsupplierid)

    # 采购——填写采购单 点击提交（已做完）
    def Order_submit_click(self):
        rowCount = self.table_order.rowCount()
        if rowCount == 0:
            QMessageBox.warning(self, '警告', '你好像还没有添加商品哦！', QMessageBox.Yes)
            return None
        if self.supplier_id.text() == "":
            QMessageBox.warning(self, '警告', '你好像还没有选择供应商哦！', QMessageBox.Yes)
            return None
        orderid = self.order_id_order_2.text()
        account = self.manager.getAccount()
        supplierid = self.supplier_id.text()
        for row in range(rowCount):
            orderleft = ordernumber = int(self.table_order.item(row, 5).text()) / int(
                self.table_order.item(row, 4).text())
            goodsid = self.table_order.item(row, 0).text()
            OrderFuc.insertOrder(
                Order(order_id=orderid, account_id=account, supplier_id=supplierid, order_left=orderleft,
                      order_date=time.strftime("%Y-%m-%d", time.localtime()), goods_id=goodsid,
                      order_flag="未入库", order_number=ordernumber))
        self.table_order.setRowCount(0)  # 设置表格行数为0，清空表格

        orderlist = OrderFuc.selectOrder()
        self.order_date.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.order_id_order_2.setText("B" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(orderlist) + 1))
        self.reload()
        QMessageBox.information(self, '提醒', '提交完成！', QMessageBox.Yes)

    # 采购——添加商品按钮（已做完）
    def purchase_addgoods(self):
        if self.supplier_id.text() == '':
            QMessageBox.warning(self, '警告', '请先选择供应商！', QMessageBox.Yes)
            return None
        goods = GoodsFuc.selectGoodsBySupplierId(self.supplier_id.text())
        # goods = GoodsFuc.selectGoods()
        if goods is None:
            QMessageBox.warning(self, '警告', '该供应商目前没有记录的商品！', QMessageBox.Yes)
            return None

        good_num = len(goods)
        self.dlg = goods_win.win()
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
            butadd.setIcon(QIcon(':/img/resource/info_icon.png'))
            butadd.goodsid = good.getGoods_id()
            butadd.clicked.connect(self.purchasing_addgoods)
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

        if self.dlg.table_goods.rowCount() == 0:
            QMessageBox.warning(self, '警告', '该供应商的商品均已被删除！', QMessageBox.Yes)
            return None
        self.dlg.show()

    # 采购——删除采购商品（已做完）
    def purchase_deletegoods(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            for row in range(self.table_order.rowCount()):
                if self.table_order.item(row, 0).text() == goodsid:
                    self.table_order.removeRow(row)
                    break

    # 采购——修改商品数量（已做完）
    def purchase_setgoodsnum(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            # 修改good列表里储存的采购单商品
            for row in range(self.table_order.rowCount()):
                if self.table_order.item(row, 0).text() == goodsid:
                    num = source.value()
                    sell = int(self.table_order.item(row, 4).text())
                    self.table_order.setItem(row, 5, QTableWidgetItem(str(num * sell)))  #
                    break

    # 采购单添加商品——槽函数（已做完）
    def purchasing_addgoods(self):
        source = self.sender()
        goodsid = source.goodsid  # 商品编号
        good = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]

        for row in range(self.table_order.rowCount()):
            if self.table_order.item(row, 0).text() == goodsid:
                QMessageBox.warning(self, '警告', '列表内已含有该商品！', QMessageBox.Yes)
                return None

        cur_row_count = self.table_order.rowCount()  # 当前行数
        cur_row_count += 1
        self.table_order.setRowCount(cur_row_count)

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
        butdelete.clicked.connect(self.purchase_deletegoods)
        widget = QWidget()
        hLayout = QHBoxLayout()
        hLayout.addWidget(butdelete)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        # 创建输入框
        # 创建spinBox
        spinBox = QSpinBox()
        spinBox.setRange(1, 999999)
        spinBox.setSingleStep(1)
        spinBox.valueChanged.connect(self.purchase_setgoodsnum)
        spinBox.goodsid = goodsid

        editwidget = QWidget()
        edithLayout = QHBoxLayout()
        edithLayout.addWidget(spinBox)
        edithLayout.setContentsMargins(5, 2, 5, 2)
        editwidget.setLayout(edithLayout)

        self.table_order.setItem(cur_row_count - 1, 0, QTableWidgetItem(good.getGoods_id()))  #
        self.table_order.setItem(cur_row_count - 1, 1, QTableWidgetItem(good.get_GoodsName()))  #
        self.table_order.setCellWidget(cur_row_count - 1, 2, editwidget)  # 采购数量（编辑框）
        self.table_order.setItem(cur_row_count - 1, 3, QTableWidgetItem(good.get_GoodsUnit()))  #
        self.table_order.setItem(cur_row_count - 1, 4, QTableWidgetItem(good.getPrice_sell()))  #
        self.table_order.setItem(cur_row_count - 1, 5, QTableWidgetItem(good.getPrice_sell()))  #
        self.table_order.setCellWidget(cur_row_count - 1, 6, widget)  # 删除按钮

        QMessageBox.information(self.dlg, '提醒', '商品\"' + good.get_GoodsName() + "\"添加成功！", QMessageBox.Yes)

    # 设置工具栏上显示的当前用户和部门 还有 填写采购单 页面的部分空格（已完成）
    def setToolbarUserinfo(self):
        userid = self.manager.getEmployee_name()
        department = self.manager.getDepartment()
        self.Current_user.setText("当前用户：" + userid)
        self.Current_department.setText("当前部门：" + department)
        self.employee_name.setText(userid)
        self.employee_name_2.setText(userid)

    # 添加供应商 获取选中的供应商（已完成）
    def getchosenSupplier(self):
        source = self.sender()
        Supplier_id = source.SupplierId_Chosed
        Supplier = SupplierFuc.selectSupplierBySupplierId(Supplier_id)[0]
        self.supplier_id.setText(Supplier.get_supplier_id())
        self.supplier_name.setText(Supplier.get_supplier_name())
        self.supplier_address.setText(Supplier.get_supplier_addr())
        self.supplier_contact.setText(Supplier.get_supplier_contactor())
        self.supplier_tel.setText(Supplier.get_supplier_phone())
        self.dlg.close()
        print(Supplier)

    # 获取采购单详情（已完成）
    def PurchasingInfo(self):
        source = self.sender()
        order_id = source.order_id  # 采购单编号
        print(source)

        self.dlg = orderinfo_win.win()
        order = OrderFuc.selectOrderByOrderId(order_id)

        self.dlg.table_order.setRowCount(len(order))  # 设置表格行数

        manager = ManagerFuc.selectManagerByAccount(order[0].get_account_id())[0]
        supplier = SupplierFuc.selectSupplierBySupplierId(order[0].get_supplier_id())[0]

        self.dlg.order_id.setText(order_id)
        self.dlg.supplier_id.setText(supplier.get_supplier_id())
        self.dlg.supplier_name.setText(supplier.get_supplier_name())
        self.dlg.supplier_add.setText(supplier.get_supplier_addr())
        self.dlg.supplier_contact.setText(supplier.get_supplier_contactor())
        self.dlg.supplier_tel.setText(supplier.get_supplier_phone())
        self.dlg.purchase_people.setText(manager.getEmployee_name())
        self.dlg.order_date.setText(str(order[0].get_order_date()))

        for index, order in enumerate(order, 0):
            goodsid = order.get_goods_id()
            goods = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]
            supplier = SupplierFuc.selectSupplierBySupplierId(goods.getSupplier_id())[0]

            # self.dlg.table_order.setItem(index, 0, QTableWidgetItem(str(index)))  #
            self.dlg.table_order.setItem(index, 0, QTableWidgetItem(goods.getGoods_id()))  #
            self.dlg.table_order.setItem(index, 1, QTableWidgetItem(goods.get_GoodsName()))  #
            self.dlg.table_order.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  #
            self.dlg.table_order.setItem(index, 3, QTableWidgetItem(str(order.get_order_number())))  #
            self.dlg.table_order.setItem(index, 4, QTableWidgetItem(goods.get_GoodsUnit()))  #
            self.dlg.table_order.setItem(index, 5, QTableWidgetItem(goods.getPrice_cost()))  #
            self.dlg.table_order.setItem(index, 6,
                                         QTableWidgetItem(
                                             str(int(goods.getPrice_cost()) * order.get_order_number())))  #
            self.dlg.table_order.setItem(index, 7, QTableWidgetItem(order.get_order_flag()))  #

        self.dlg.show()

    # 当采购页面的BOX切换（已完成）
    def Box_purchasing_changed(self):
        if self.Box_purchasing.currentIndex() == 0:  # 切换成了填写采购单页
            print("切换成了填写采购单页")
        elif self.Box_purchasing.currentIndex() == 1:
            # 采购管理——采购单查询
            orderinfo = OrderFuc.selectOrder()
            if orderinfo is None: orderinfo = []
            self.table_orderinfo.setRowCount(len(orderinfo))  # 设置表格行数

            self.but_info = []
            for index, item in enumerate(orderinfo, 0):
                supplier_id = item.get_supplier_id()
                account_id = item.get_account_id()

                supplier = SupplierFuc.selectSupplierBySupplierId(supplier_id)
                manage = ManagerFuc.selectManagerByAccount(account_id)

                butinfo_temp = QPushButton("详情")
                self.but_info.append(butinfo_temp)
                butinfo_temp.setDown(True)
                butinfo_temp.setStyleSheet(''' text-align : center;
                                                  border: 2px solid #e7e7e7;
                                                  height : 30px;
                                                  border-top:1px solid #eee;
                                                  font : 13px;''')
                butinfo_temp.setIcon(QIcon(':/img/resource/info_icon.png'))
                butinfo_temp.order_id = item.get_order_id()
                butinfo_temp.clicked.connect(self.PurchasingInfo)

                widget = QWidget()
                hLayout = QHBoxLayout()
                hLayout.addWidget(self.but_info[index])
                hLayout.setContentsMargins(5, 2, 5, 2)
                widget.setLayout(hLayout)

                self.table_orderinfo.setItem(index, 0, QTableWidgetItem(item.get_order_id()))  # 采购单编号
                self.table_orderinfo.setItem(index, 1, QTableWidgetItem(supplier[0].get_supplier_name()))  # 供应商名称
                self.table_orderinfo.setItem(index, 2, QTableWidgetItem(manage[0].getEmployee_name()))  # 负责人
                self.table_orderinfo.setItem(index, 3,
                                             QTableWidgetItem(item.get_order_date().strftime('%Y-%m-%d')))  # 订单日期

                self.table_orderinfo.setCellWidget(index, 4, widget)  # 操作

            print(orderinfo)

            print("切换成了采购单查询页")

        elif self.Box_purchasing.currentIndex() == 2:
            self.draftOrder_research()

    # 按下添加供应商按钮（已完成）
    def supplier_add_click(self):
        self.dlg = supplier_win.win()
        # self.wid.pushButton.clicked.connect(self.GetLine)
        supplierinfo = SupplierFuc.selectSupplier()
        self.dlg.table_supplier.horizontalHeader().setStyleSheet("""QHeaderView::section {background-color:#008CBA ; /* 蓝色 */
                                                                color: WHITE;
                                                                };
                                                                text-align : center;""")
        for index, item in enumerate(supplierinfo, 0):
            if item.get_isdelete() == 1:  #
                continue
            currentcount = self.dlg.table_supplier.rowCount()
            self.dlg.table_supplier.setRowCount(currentcount + 1)  # 设置表格行数+1

            id = item.get_supplier_id()
            name = item.get_supplier_name()
            contactor = item.get_supplier_contactor()
            phone = item.get_supplier_phone()
            add = item.get_supplier_addr()

            supplierAddtemp = QPushButton("确定")
            supplierAddtemp.SupplierId_Chosed = id
            supplierAddtemp.setDown(True)
            supplierAddtemp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            supplierAddtemp.setIcon(QIcon(':/img/resource/add_icon.png'))
            supplierAddtemp.clicked.connect(self.getchosenSupplier)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(supplierAddtemp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_supplier.setItem(currentcount, 0, QTableWidgetItem(id))  # 供应商编号
            self.dlg.table_supplier.setItem(currentcount, 1, QTableWidgetItem(name))  # 供应商名称
            self.dlg.table_supplier.setItem(currentcount, 2, QTableWidgetItem(contactor))  # 负责人
            self.dlg.table_supplier.setItem(currentcount, 3, QTableWidgetItem(phone))  # 联系人电话
            self.dlg.table_supplier.setItem(currentcount, 4, QTableWidgetItem(add))  # 供应商地址
            self.dlg.table_supplier.setCellWidget(currentcount, 5, widget)  # 操作

        self.dlg.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InvoiceSystem(MainWindow, Manager(1, 1, "采购员", "采购部门"))  # 注意把类名修改为myDialog
    # ui.setupUi(MainWindow)  myDialog类的构造函数已经调用了这个函数，这行代码可以删去
    MainWindow.show()
    sys.exit(app.exec_())
