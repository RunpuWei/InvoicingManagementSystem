# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supplierinfo_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1021, 702)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/supplier_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 671))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_9.addWidget(self.label_39)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_40 = QtWidgets.QLabel(self.layoutWidget)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_14.addWidget(self.label_40)
        self.supplierid = QtWidgets.QLineEdit(self.layoutWidget)
        self.supplierid.setObjectName("supplierid")
        self.horizontalLayout_14.addWidget(self.supplierid)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_14.addWidget(self.label_41)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.horizontalLayout_14.addWidget(self.name)
        self.search = QtWidgets.QPushButton(self.layoutWidget)
        self.search.setMinimumSize(QtCore.QSize(0, 30))
        self.search.setObjectName("search")
        self.horizontalLayout_14.addWidget(self.search)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.table_supplier = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_supplier.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_supplier.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_supplier.setObjectName("table_supplier")
        self.table_supplier.setColumnCount(6)
        self.table_supplier.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier.setHorizontalHeaderItem(5, item)
        self.verticalLayout_9.addWidget(self.table_supplier)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "供应商选择界面"))
        self.label_39.setText(_translate("Form", "供应商信息"))
        self.label_40.setText(_translate("Form", "供应商编号："))
        self.label_41.setText(_translate("Form", "供应商名称:"))
        self.search.setText(_translate("Form", "搜索"))
        item = self.table_supplier.horizontalHeaderItem(0)
        item.setText(_translate("Form", "供应商编号"))
        item = self.table_supplier.horizontalHeaderItem(1)
        item.setText(_translate("Form", "供应商姓名"))
        item = self.table_supplier.horizontalHeaderItem(2)
        item.setText(_translate("Form", "供应商联系人"))
        item = self.table_supplier.horizontalHeaderItem(3)
        item.setText(_translate("Form", "联系人电话"))
        item = self.table_supplier.horizontalHeaderItem(4)
        item.setText(_translate("Form", "供应商地址"))
        item = self.table_supplier.horizontalHeaderItem(5)
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

