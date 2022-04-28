# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addGoods_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 558)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/Goods_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 1031, 521))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_6.addWidget(self.label_25)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_26.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        self.goodsid_goods = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.goodsid_goods.setMaximumSize(QtCore.QSize(200, 16777215))
        self.goodsid_goods.setObjectName("goodsid_goods")
        self.horizontalLayout_8.addWidget(self.goodsid_goods)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_27.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_8.addWidget(self.label_27)
        self.goodsname_goods = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.goodsname_goods.setMaximumSize(QtCore.QSize(200, 16777215))
        self.goodsname_goods.setObjectName("goodsname_goods")
        self.horizontalLayout_8.addWidget(self.goodsname_goods)
        self.search_goods = QtWidgets.QPushButton(self.layoutWidget_4)
        self.search_goods.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_goods.setObjectName("search_goods")
        self.horizontalLayout_8.addWidget(self.search_goods)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.table_goods = QtWidgets.QTableWidget(self.layoutWidget_4)
        self.table_goods.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_goods.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_goods.setObjectName("table_goods")
        self.table_goods.setColumnCount(8)
        self.table_goods.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(7, item)
        self.verticalLayout_6.addWidget(self.table_goods)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "商品添加页面"))
        self.label_25.setText(_translate("Form", "商品信息"))
        self.label_26.setText(_translate("Form", "商品编号："))
        self.goodsid_goods.setPlaceholderText(_translate("Form", "无"))
        self.label_27.setText(_translate("Form", "商品名称："))
        self.goodsname_goods.setPlaceholderText(_translate("Form", "无"))
        self.search_goods.setText(_translate("Form", "搜索"))
        item = self.table_goods.horizontalHeaderItem(0)
        item.setText(_translate("Form", "商品编号"))
        item = self.table_goods.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.table_goods.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品单位"))
        item = self.table_goods.horizontalHeaderItem(3)
        item.setText(_translate("Form", "供应商"))
        item = self.table_goods.horizontalHeaderItem(4)
        item.setText(_translate("Form", "销售单价/元"))
        item = self.table_goods.horizontalHeaderItem(5)
        item.setText(_translate("Form", "库存数量"))
        item = self.table_goods.horizontalHeaderItem(6)
        item.setText(_translate("Form", "成本单价/元"))
        item = self.table_goods.horizontalHeaderItem(7)
        item.setText(_translate("Form", "操作"))

import main_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

