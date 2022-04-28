# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Salelist_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 971, 551))
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
        self.order_id_saleinfo = QtWidgets.QLineEdit(self.layoutWidget)
        self.order_id_saleinfo.setObjectName("order_id_saleinfo")
        self.horizontalLayout_5.addWidget(self.order_id_saleinfo)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.customer_id_saleinfo = QtWidgets.QLineEdit(self.layoutWidget)
        self.customer_id_saleinfo.setObjectName("customer_id_saleinfo")
        self.horizontalLayout_5.addWidget(self.customer_id_saleinfo)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.search_saleinfo = QtWidgets.QPushButton(self.layoutWidget)
        self.search_saleinfo.setMinimumSize(QtCore.QSize(0, 30))
        self.search_saleinfo.setObjectName("search_saleinfo")
        self.horizontalLayout_5.addWidget(self.search_saleinfo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.table_saleinfo = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_saleinfo.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_saleinfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_saleinfo.setObjectName("table_saleinfo")
        self.table_saleinfo.setColumnCount(5)
        self.table_saleinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_saleinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_saleinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_saleinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_saleinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_saleinfo.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.table_saleinfo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "销售单查询"))
        self.label_12.setText(_translate("Form", "销售单查询"))
        self.label_13.setText(_translate("Form", "订单编号："))
        self.order_id_saleinfo.setPlaceholderText(_translate("Form", "无"))
        self.label_14.setText(_translate("Form", "顾客编号："))
        self.customer_id_saleinfo.setPlaceholderText(_translate("Form", "无"))
        self.label_15.setText(_translate("Form", "订单时间："))
        self.comboBox.setItemText(0, _translate("Form", "无"))
        self.comboBox.setItemText(1, _translate("Form", "三天内"))
        self.comboBox.setItemText(2, _translate("Form", "一周内"))
        self.comboBox.setItemText(3, _translate("Form", "一个月内"))
        self.search_saleinfo.setText(_translate("Form", "搜索"))
        item = self.table_saleinfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "销售单编号"))
        item = self.table_saleinfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "顾客名称"))
        item = self.table_saleinfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "负责人"))
        item = self.table_saleinfo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "订单日期"))
        item = self.table_saleinfo.horizontalHeaderItem(4)
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

