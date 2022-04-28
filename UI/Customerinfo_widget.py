# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Customerinfo_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(991, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/customer_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 971, 521))
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
        self.customer_id = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.customer_id.setMaximumSize(QtCore.QSize(200, 16777215))
        self.customer_id.setObjectName("customer_id")
        self.horizontalLayout_8.addWidget(self.customer_id)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_27.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_8.addWidget(self.label_27)
        self.customer_name = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.customer_name.setMaximumSize(QtCore.QSize(200, 16777215))
        self.customer_name.setObjectName("customer_name")
        self.horizontalLayout_8.addWidget(self.customer_name)
        self.search_user = QtWidgets.QPushButton(self.layoutWidget_4)
        self.search_user.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_user.setObjectName("search_user")
        self.horizontalLayout_8.addWidget(self.search_user)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.table_customer = QtWidgets.QTableWidget(self.layoutWidget_4)
        self.table_customer.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_customer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_customer.setObjectName("table_customer")
        self.table_customer.setColumnCount(5)
        self.table_customer.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_customer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_customer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_customer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_customer.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_customer.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.table_customer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加顾客信息"))
        self.label_25.setText(_translate("Form", "顾客信息"))
        self.label_26.setText(_translate("Form", "顾客编号："))
        self.customer_id.setPlaceholderText(_translate("Form", "无"))
        self.label_27.setText(_translate("Form", "顾客名称："))
        self.customer_name.setPlaceholderText(_translate("Form", "无"))
        self.search_user.setText(_translate("Form", "搜索"))
        item = self.table_customer.horizontalHeaderItem(0)
        item.setText(_translate("Form", "顾客编号"))
        item = self.table_customer.horizontalHeaderItem(1)
        item.setText(_translate("Form", "顾客姓名"))
        item = self.table_customer.horizontalHeaderItem(2)
        item.setText(_translate("Form", "顾客电话"))
        item = self.table_customer.horizontalHeaderItem(3)
        item.setText(_translate("Form", "送货地址"))
        item = self.table_customer.horizontalHeaderItem(4)
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

