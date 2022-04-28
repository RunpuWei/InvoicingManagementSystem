import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QPushButton, QHBoxLayout, QTableWidgetItem, QSpinBox

from UI import user_warehouse
from func import OrderFuc, SupplierFuc, ManagerFuc, GoodsFuc, ReturnFuc, OutboundFuc, InboundFuc, SaleFuc, CustomerFuc
from user import widget_Salelist as salelist_win
from user import widget_Outboundinfo as outboundinfo_win
from user import widget_Purchaseorderquery_win as purchaseorderquery_win
from vo.Inbound import Inbound
from vo.Manager import Manager
from vo.Outbound import Outbound
import sys


class InvoiceSystem(QMainWindow, user_warehouse.Ui_mainWindow):  # 继承自Ui_mainWindow类
    def __init__(self, mainWindow, manager=None):
        super().__init__()
        self.setupUi(mainWindow)  # 调用父类的setupUI函数
        self.setFixedSize(self.width(), self.height())
        self.statusbar.showMessage('登陆成功！', 3000)  # 信息显示3秒
        self.manager = manager
        self.setToolbarUserinfo()

        self.related_sale_outbound.clicked.connect(self.related_sale_click)
        self.outbound_submit.clicked.connect(self.submit_outbound_click)
        self.but_purchasing_inbound.clicked.connect(self.related_purchase_click)
        self.inbound_submit.clicked.connect(self.inbound_submit_clicked)
        # self.sale_goods_add.clicked.connect(self.button_addgoods)

    # 盘库 按下修改商品库存数量按钮
    def but_modifyGoodsnum_clicked(self):
        source = self.sender()
        goodsid = source.goodsid
        for item in self.goodlist:
            if item.getGoods_id() == goodsid:
                if GoodsFuc.updateGoodsNumber(item):
                    QMessageBox.information(self, '提醒', '商品\"' + item.get_GoodsName() + "\"库存数量修改成功！", QMessageBox.Yes)
                    self.table_kucun.setRowCount(0)
                    self.kucun_research()
                break

    # 盘库 修改商品库存数量spinbox
    def modifyGoodsnum(self):
        source = self.sender()
        goodsid = source.goodsid
        for item in self.goodlist:
            if item.getGoods_id() == goodsid:
                item.setGoods_number(source.value())
                break

    # 盘库 加载商品库存信息
    def kucun_research(self):
        goodlist_temp = GoodsFuc.selectGoods()
        self.goodlist = []
        for item in goodlist_temp:
            if item.get_isdelete() == 0:
                self.goodlist.append(item)

        self.table_kucun.setRowCount(len(self.goodlist))
        for index, item in enumerate(self.goodlist, 0):
            # 创建spinBox
            spinBox = QSpinBox()
            spinBox.setRange(0, 999999)
            spinBox.setValue(item.getGoods_number())
            spinBox.setSingleStep(1)
            spinBox.valueChanged.connect(self.modifyGoodsnum)
            spinBox.goodsid = item.getGoods_id()  # 把商品编号赋值给spinbox

            editwidget = QWidget()
            edithLayout = QHBoxLayout()
            edithLayout.addWidget(spinBox)
            edithLayout.setContentsMargins(5, 2, 5, 2)
            editwidget.setLayout(edithLayout)

            butinfo_temp = QPushButton("修改数量")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/modify_icon.png'))
            butinfo_temp.goodsid = item.getGoods_id()
            butinfo_temp.clicked.connect(self.but_modifyGoodsnum_clicked)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_kucun.setItem(index, 0, QTableWidgetItem(item.getGoods_id()))  # 商品编号
            self.table_kucun.setItem(index, 1, QTableWidgetItem(item.get_GoodsName()))  # 名称
            self.table_kucun.setItem(index, 2, QTableWidgetItem(item.get_GoodsUnit()))  # 单位
            self.table_kucun.setItem(index, 3, QTableWidgetItem(item.getSupplier_id()))  # 供应商
            self.table_kucun.setCellWidget(index, 4, editwidget)  # 库存数量
            self.table_kucun.setItem(index, 5, QTableWidgetItem(item.getPrice_sell()))  # 销售单价
            self.table_kucun.setItem(index, 6, QTableWidgetItem(item.getPrice_cost()))  # 成本单价
            self.table_kucun.setCellWidget(index, 7, widget)  # 操作

    # 点击关联采购单按钮
    def related_purchase_click(self):
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
            butinfo_temp.clicked.connect(self.chosenRelatedPurchase)

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

    # 按下了入库单的提交按钮
    def inbound_submit_clicked(self):
        rowCount = self.table_inbound.rowCount()  # 入库单行数
        if rowCount == 0:
            QMessageBox.warning(self, '警告', '入库单为空，请重新选择关联采购单再试！', QMessageBox.Yes)
            return None

        inbound_id = self.inbound_id_inbound.text()
        order_id = self.purchasing_id.text()
        account_id = self.manager.getAccount()
        date = self.date_inbound.text()

        orderlist = OrderFuc.selectOrderByOrderId(order_id)
        for row in range(rowCount):
            goodsid = self.table_inbound.item(row, 0).text()
            in_num = int(self.table_inbound.item(row, 6).text()) - int(self.table_inbound.item(row, 5).text())

            good = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]
            good.setGoods_number(self.table_inbound.item(row, 6).text())  # 更新库存数量

            # 获取对应商品的销售单
            for i in orderlist:
                if i.get_goods_id() == goodsid:
                    order = i
                    break
            order_newleft = int(self.table_inbound.item(row, 4).text()) - in_num
            order.set_order_left(order_newleft)
            if order_newleft == 0:
                order.set_order_flag("已入库")
            else:
                order.set_order_flag("未入库数量：" + str(order_newleft))

            InboundFuc.insertInbound(Inbound(inbound_id, order_id, goodsid, account_id, date, in_num))
            GoodsFuc.updateGoodsNumber(good)
            OrderFuc.updateOrderFlag(order)

        self.table_inbound.setRowCount(0)  # 设置表格行数为0，清空表格
        inboundlist = InboundFuc.selectInbound()
        self.date_inbound.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.inbound_id_inbound.setText(
            "I" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(inboundlist) + 1))
        QMessageBox.information(self, '提醒', '入库单提交完成！', QMessageBox.Yes)

    # 关联采购单信息
    def chosenRelatedPurchase(self):
        source = self.sender()
        orderlist_temp = OrderFuc.selectOrderByOrderId(source.order_id)
        orderlist = []

        for item in orderlist_temp:
            if not (item.get_order_flag() == "已入库" or item.get_order_flag() == "已退货"):
                orderlist.append(item)

        if len(orderlist) == 0:
            QMessageBox.warning(self, '警告', '该采购单已入库完毕！', QMessageBox.Yes)
            return None

        self.purchasing_id.setText(source.order_id)  # 填入关联采购单编号栏
        self.dlg.close()
        self.table_inbound.setRowCount(len(orderlist))  # 设置表格行数

        for index, item in enumerate(orderlist, 0):
            goods_id = item.get_goods_id()
            goods = GoodsFuc.selectGoodsByGoodsId(goods_id)[0]
            supplier_id = item.get_supplier_id()
            supplier = \
                SupplierFuc.selectSupplierBySupplierId(GoodsFuc.selectGoodsByGoodsId(goods_id)[0].getSupplier_id())[0]
            order_id = item.get_order_id()

            # 创建spinBox
            spinBox = QSpinBox()
            spinBox.setRange(0, item.get_order_left())
            spinBox.setSingleStep(1)
            spinBox.valueChanged.connect(self.inbound_setgoodsnum)
            spinBox.goodsid = item.get_goods_id()  # 把商品编号赋值给spinbox

            editwidget = QWidget()
            edithLayout = QHBoxLayout()
            edithLayout.addWidget(spinBox)
            edithLayout.setContentsMargins(5, 2, 5, 2)
            editwidget.setLayout(edithLayout)

            butinfo_temp = QPushButton("删除")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/delete_icon.png'))

            butinfo_temp.goods_id = item.get_goods_id()  # 把商品编号赋值给按钮
            butinfo_temp.clicked.connect(self.inbound_deletegoods)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_inbound.setItem(index, 0, QTableWidgetItem(goods_id))  # 商品编号
            self.table_inbound.setItem(index, 1, QTableWidgetItem(goods.get_GoodsName()))  # 商品名称
            self.table_inbound.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  # 商品供应商
            self.table_inbound.setCellWidget(index, 3, editwidget)  # goodsnum

            self.table_inbound.setItem(index, 4, QTableWidgetItem(str(item.get_order_left())))  # goodsleft
            self.table_inbound.setItem(index, 5, QTableWidgetItem(str(goods.getGoods_number())))  # goodsku
            self.table_inbound.setItem(index, 6, QTableWidgetItem(str(goods.getGoods_number())))  # 预计剩余库存
            self.table_inbound.setItem(index, 7, QTableWidgetItem(goods.get_GoodsUnit()))  # 商品单位
            self.table_inbound.setCellWidget(index, 8, widget)  # 操作

    # 入库——删除入库商品（已做完）
    def inbound_deletegoods(self):
        source = self.sender()
        if source:
            goodsid = source.goods_id
            for row in range(self.table_inbound.rowCount()):
                if self.table_inbound.item(row, 0).text() == goodsid:
                    self.table_inbound.removeRow(row)
                    break

    # 入库——修改入库商品数量
    def inbound_setgoodsnum(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            for row in range(self.table_inbound.rowCount()):
                if self.table_inbound.item(row, 0).text() == goodsid:
                    num = source.value()
                    kucun = int(self.table_inbound.item(row, 5).text())  # 当前库存
                    self.table_inbound.setItem(row, 6, QTableWidgetItem(str(kucun + num)))  # 预计剩余库存
                    break

    # 出库单查询
    def outbound_research(self):
        outboundlist = OutboundFuc.selectOutbound()
        if outboundlist is None: outboundlist = []
        self.table_outboundinfo.setRowCount(len(outboundlist))  # 设置表格行数
        for index, item in enumerate(outboundlist, 0):
            manager = ManagerFuc.selectManagerByAccount(item.get_account_id())[0]
            sale = SaleFuc.selectSaleBySaleId(item.get_sale_id())[0]
            customer = CustomerFuc.selectCustomerByCustomerId(sale.get_customer_id())[0]

            butinfo_temp = QPushButton("详情")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(":/img/resource/info_icon.png"))
            butinfo_temp.out_id = item.get_out_id()
            butinfo_temp.clicked.connect(self.getchosenOutboundinfo)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_outboundinfo.setItem(index, 0, QTableWidgetItem(item.get_out_id()))  # 出库单编号
            self.table_outboundinfo.setItem(index, 1, QTableWidgetItem(customer.getCustomer_name()))  # 顾客名称
            self.table_outboundinfo.setItem(index, 2, QTableWidgetItem(manager.getEmployee_name()))  # 负责人
            self.table_outboundinfo.setItem(index, 3,
                                            QTableWidgetItem(item.get_out_date().strftime('%Y-%m-%d')))  # 出库单日期
            self.table_outboundinfo.setCellWidget(index, 4, widget)  # 操作

    def getchosenOutboundinfo(self):
        outid = self.sender().out_id  # 出库单编号

        outboundlist = OutboundFuc.selectOutboundByOutboundId(outid)
        manager = ManagerFuc.selectManagerByAccount(outboundlist[0].get_account_id())[0]
        sale = SaleFuc.selectSaleBySaleId(outboundlist[0].get_sale_id())[0]
        customer = CustomerFuc.selectCustomerByCustomerId(sale.get_customer_id())[0]

        self.dlg = outboundinfo_win.win()
        self.dlg.out_id.setText(outid)
        self.dlg.relatedSaleid.setText(sale.get_sale_id())
        self.dlg.customer_id.setText(customer.getCustomer_id())
        self.dlg.customer_name.setText(customer.getCustomer_name())
        self.dlg.customer_phone.setText(customer.getCustomer_phone())
        self.dlg.customer_addr.setText(customer.getCustomer_address())
        self.dlg.sale_people.setText(manager.getEmployee_name())
        self.dlg.sale_date.setText(str(outboundlist[0].get_out_date()))

        self.dlg.table_outbound.setRowCount(len(outboundlist))  # 设置表格行数
        for index, item in enumerate(outboundlist, 0):
            goodsid = item.get_goods_id()
            goods = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]
            supplier = SupplierFuc.selectSupplierBySupplierId(goods.getSupplier_id())[0]

            self.dlg.table_outbound.setItem(index, 0, QTableWidgetItem(goods.getGoods_id()))  #
            self.dlg.table_outbound.setItem(index, 1, QTableWidgetItem(goods.get_GoodsName()))  #
            self.dlg.table_outbound.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  #
            self.dlg.table_outbound.setItem(index, 3, QTableWidgetItem(str(item.get_out_num())))  #
            self.dlg.table_outbound.setItem(index, 4, QTableWidgetItem(goods.get_GoodsUnit()))  #
            self.dlg.table_outbound.setItem(index, 5, QTableWidgetItem(goods.getPrice_sell()))  #
            self.dlg.table_outbound.setItem(index, 6,
                                            QTableWidgetItem(
                                                str(int(goods.getPrice_sell()) * item.get_out_num())))  #
            self.dlg.table_outbound.setItem(index, 7, QTableWidgetItem(item.get_out_flag()))  #

        self.dlg.show()

    # 点下出库提交按钮
    def submit_outbound_click(self):
        rowCount = self.table_outbound.rowCount()
        if rowCount == 0:
            QMessageBox.warning(self, '警告', '出库单为空，请重新选择关联销售单再试！', QMessageBox.Yes)
            return None
        outid = self.outid_outbound.text()
        relatedSale_ID = self.relatedSale_ID_outbound.text()
        account = self.manager.getAccount()
        date = self.date_outbound.text()
        salelist = SaleFuc.selectSaleBySaleId(relatedSale_ID)
        for row in range(rowCount):
            goodsid = self.table_outbound.item(row, 0).text()

            # 获取对应商品的销售单
            for i in salelist:
                if i.get_goods_id() == goodsid:
                    sale = i
                    break

            good = GoodsFuc.selectGoodsByGoodsId(goodsid)[0]
            goods_out = int(self.table_outbound.item(row, 5).text()) - int(
                self.table_outbound.item(row, 6).text())  # 出库数量=当前商品库存-预期剩余库存
            goods_left = int(self.table_outbound.item(row, 4).text())  # 待出库数量
            goods_oldku = int(self.table_outbound.item(row, 5).text())  # 商品库存
            goods_newku = int(self.table_outbound.item(row, 6).text())
            goods_newleft = goods_left - goods_out

            good.setGoods_number(goods_newku)  # 更新商品库存数量
            sale.set_sale_left(goods_newleft)  # 更新销售单未发货数量
            if goods_newleft == 0:
                sale.set_sale_flag("已出库")
            else:
                sale.set_sale_flag("未出库数量：" + str(goods_newleft))

            OutboundFuc.insertOutbound(Outbound(outid, relatedSale_ID, account, date, goodsid, goods_out, "未发货"))
            GoodsFuc.updateGoodsNumber(good)
            SaleFuc.updateSale_outNumber(sale)

        self.table_outbound.setRowCount(0)  # 设置表格行数为0，清空表格
        self.outbound_research()
        outboundlist = OutboundFuc.selectOutbound()
        self.date_outbound.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.outid_outbound.setText("O" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(outboundlist) + 1))

        QMessageBox.information(self, '提醒', '出库单提交完成！', QMessageBox.Yes)

    # 关联销售单信息
    def chosenRelatedSale(self):
        source = self.sender()
        self.relatedSale_ID_outbound.setText(source.sale_id)
        salelist_temp = SaleFuc.selectSaleBySaleId(source.sale_id)
        salelist = []
        for item in salelist_temp:
            if item.get_sale_flag() != "已出库":
                salelist.append(item)

        if len(salelist) == 0:
            QMessageBox.warning(self, '警告', '该销售单已出库完毕！', QMessageBox.Yes)
            return None

        self.table_outbound.setRowCount(len(salelist))
        for index, item in enumerate(salelist, 0):
            goodid = item.get_goods_id()
            good = GoodsFuc.selectGoodsByGoodsId(goodid)[0]
            supplier = SupplierFuc.selectSupplierBySupplierId(good.getSupplier_id())[0]

            # 创建spinBox
            spinBox = QSpinBox()
            spinBox.setRange(0, min(int(item.get_sale_left()), int(good.getGoods_number())))
            spinBox.setSingleStep(1)
            spinBox.valueChanged.connect(self.outbound_setgoodsnum)
            spinBox.goodsid = goodid

            editwidget = QWidget()
            edithLayout = QHBoxLayout()
            edithLayout.addWidget(spinBox)
            edithLayout.setContentsMargins(5, 2, 5, 2)
            editwidget.setLayout(edithLayout)

            # 创建删除按钮
            butdelete = QPushButton("删除")
            butdelete.setDown(True)
            butdelete.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butdelete.setIcon(QIcon(':/img/resource/delete_icon.png'))
            butdelete.goodsid = goodid
            butdelete.clicked.connect(self.outbound_deletegoods)
            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butdelete)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.table_outbound.setItem(index, 0, QTableWidgetItem(goodid))  # 商品编号
            self.table_outbound.setItem(index, 1, QTableWidgetItem(good.get_GoodsName()))  # 商品名称
            self.table_outbound.setItem(index, 2, QTableWidgetItem(supplier.get_supplier_name()))  # 商品供应商
            self.table_outbound.setCellWidget(index, 3, editwidget)  # 出库数量（编辑框）
            self.table_outbound.setItem(index, 4, QTableWidgetItem(str(item.get_sale_left())))  # 待出库数量
            self.table_outbound.setItem(index, 5, QTableWidgetItem(str(good.getGoods_number())))  # 商品库存
            self.table_outbound.setItem(index, 6, QTableWidgetItem(str(good.getGoods_number())))  # 预计剩余库存
            self.table_outbound.setItem(index, 7, QTableWidgetItem(good.get_GoodsUnit()))  # 商品单位
            self.table_outbound.setItem(index, 8, QTableWidgetItem(good.getPrice_sell()))  # 销售单价
            self.table_outbound.setCellWidget(index, 9, widget)  # 操作

        self.dlg.close()

    # 出库——修改出库商品数量
    def outbound_setgoodsnum(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            for row in range(self.table_outbound.rowCount()):
                if self.table_outbound.item(row, 0).text() == goodsid:
                    num = source.value()
                    kucun = int(self.table_outbound.item(row, 5).text())  # 当前库存
                    self.table_outbound.setItem(row, 6, QTableWidgetItem(str(kucun - num)))  # 预计剩余库存
                    break

    # 出库——删除商品
    def outbound_deletegoods(self):
        source = self.sender()
        if source:
            goodsid = source.goodsid
            for row in range(self.table_outbound.rowCount()):
                if self.table_outbound.item(row, 0).text() == goodsid:
                    self.table_outbound.removeRow(row)
                    break

    def related_sale_click(self):
        self.dlg = salelist_win.win()
        salelist = SaleFuc.selectSale()
        if salelist is None:
            salelist = []
        self.dlg.table_saleinfo.setRowCount(len(salelist))  # 设置表格行数
        for index, item in enumerate(salelist, 0):
            butinfo_temp = QPushButton("确定")
            butinfo_temp.setDown(True)
            butinfo_temp.setStyleSheet(''' text-align : center;
                                              border: 2px solid #e7e7e7;
                                              height : 30px;
                                              border-top:1px solid #eee;
                                              font : 13px;''')
            butinfo_temp.setIcon(QIcon(':/img/resource/add_icon.png'))
            butinfo_temp.sale_id = item.get_sale_id()
            butinfo_temp.clicked.connect(self.chosenRelatedSale)

            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(butinfo_temp)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)

            self.dlg.table_saleinfo.setItem(index, 0, QTableWidgetItem(item.get_sale_id()))  # 销售单编号
            self.dlg.table_saleinfo.setItem(index, 1, QTableWidgetItem(
                CustomerFuc.selectCustomerByCustomerId(item.get_customer_id())[0].getCustomer_name()))  # 顾客名称
            self.dlg.table_saleinfo.setItem(index, 2, QTableWidgetItem(
                ManagerFuc.selectManagerByAccount(item.get_account_id())[0].getEmployee_name()))  # 负责人
            self.dlg.table_saleinfo.setItem(index, 3,
                                            QTableWidgetItem(item.get_sale_date().strftime('%Y-%m-%d')))  # 订单日期
            self.dlg.table_saleinfo.setCellWidget(index, 4, widget)  # 操作

        self.dlg.show()

    # 设置工具栏上显示的当前用户和部门 还有 填写采购单 页面的部分空格（已完成）
    def setToolbarUserinfo(self):
        userid = self.manager.getEmployee_name()
        department = self.manager.getDepartment()
        self.Current_user.setText("当前用户：" + userid)
        self.Current_department.setText("当前部门：" + department)
        self.person_outbound.setText(userid)
        self.employee_name_inbound.setText(userid)
        self.reload()

    # 重新加载输入框默认值（已做完）
    def reload(self):
        self.table_outboundinfo.setRowCount(0)
        self.table_kucun.setRowCount(0)

        self.outbound_research()
        self.kucun_research()

        outboundlist = OutboundFuc.selectOutbound()
        if outboundlist is None: outboundlist = []
        self.date_outbound.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.outid_outbound.setText("O" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(outboundlist) + 1))

        inboundlist = InboundFuc.selectInbound()
        if inboundlist is None: inboundlist = []
        self.date_inbound.setText(time.strftime("%Y-%m-%d", time.localtime()))
        self.inbound_id_inbound.setText(
            "I" + str(int(time.strftime("%Y%m0000", time.localtime())) + len(inboundlist) + 1))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InvoiceSystem(MainWindow, Manager(2, 2, "销售员", "销售部门"))  # 注意把类名修改为myDialog
    # ui.setupUi(MainWindow)  myDialog类的构造函数已经调用了这个函数，这行代码可以删去
    MainWindow.show()
    sys.exit(app.exec_())
