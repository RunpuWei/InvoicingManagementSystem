# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Outboundlist_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 584)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/outbound_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.outbound_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.outbound_id.setObjectName("outbound_id")
        self.horizontalLayout_5.addWidget(self.outbound_id)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.saleinfo_outbound = QtWidgets.QLineEdit(self.layoutWidget)
        self.saleinfo_outbound.setObjectName("saleinfo_outbound")
        self.horizontalLayout_5.addWidget(self.saleinfo_outbound)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.time_outbound = QtWidgets.QLineEdit(self.layoutWidget)
        self.time_outbound.setObjectName("time_outbound")
        self.horizontalLayout_5.addWidget(self.time_outbound)
        self.search_outbound = QtWidgets.QPushButton(self.layoutWidget)
        self.search_outbound.setMinimumSize(QtCore.QSize(0, 30))
        self.search_outbound.setObjectName("search_outbound")
        self.horizontalLayout_5.addWidget(self.search_outbound)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.table_outboundinfo = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_outboundinfo.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.table_outboundinfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_outboundinfo.setObjectName("table_outboundinfo")
        self.table_outboundinfo.setColumnCount(5)
        self.table_outboundinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_outboundinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outboundinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outboundinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outboundinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outboundinfo.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.table_outboundinfo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关联出库单"))
        self.label_12.setText(_translate("Form", "出库单查询"))
        self.label_13.setText(_translate("Form", "出库单编号："))
        self.label_14.setText(_translate("Form", "销售单编号："))
        self.label_15.setText(_translate("Form", "订单时间："))
        self.search_outbound.setText(_translate("Form", "搜索"))
        item = self.table_outboundinfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "订单编号"))
        item = self.table_outboundinfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "顾客名称"))
        item = self.table_outboundinfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "负责人"))
        item = self.table_outboundinfo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "订单日期"))
        item = self.table_outboundinfo.horizontalHeaderItem(4)
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

