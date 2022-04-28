# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Purchaseorderquery_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(990, 556)
        Form.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 971, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.order_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.order_id.setObjectName("order_id")
        self.horizontalLayout_5.addWidget(self.order_id)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.supplier_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.supplier_id.setObjectName("supplier_id")
        self.horizontalLayout_5.addWidget(self.supplier_id)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.ordertime = QtWidgets.QComboBox(self.layoutWidget)
        self.ordertime.setMinimumSize(QtCore.QSize(120, 0))
        self.ordertime.setObjectName("ordertime")
        self.ordertime.addItem("")
        self.ordertime.addItem("")
        self.ordertime.addItem("")
        self.ordertime.addItem("")
        self.horizontalLayout_5.addWidget(self.ordertime)
        self.search = QtWidgets.QPushButton(self.layoutWidget)
        self.search.setObjectName("search")
        self.horizontalLayout_5.addWidget(self.search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.table_orderinfo = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_orderinfo.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_orderinfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_orderinfo.setObjectName("table_orderinfo")
        self.table_orderinfo.setColumnCount(5)
        self.table_orderinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_orderinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_orderinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_orderinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_orderinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_orderinfo.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.table_orderinfo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "采购单查询"))
        self.label_12.setText(_translate("Form", "采购单查询"))
        self.label_13.setText(_translate("Form", "订单编号："))
        self.label_14.setText(_translate("Form", "供应商编号："))
        self.label_15.setText(_translate("Form", "订单时间："))
        self.ordertime.setItemText(0, _translate("Form", "无"))
        self.ordertime.setItemText(1, _translate("Form", "3天内"))
        self.ordertime.setItemText(2, _translate("Form", "一周内"))
        self.ordertime.setItemText(3, _translate("Form", "一个月内"))
        self.search.setText(_translate("Form", "搜索"))
        item = self.table_orderinfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "采购单编号"))
        item = self.table_orderinfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "供应商"))
        item = self.table_orderinfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "负责人"))
        item = self.table_orderinfo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "订单日期"))
        item = self.table_orderinfo.horizontalHeaderItem(4)
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

