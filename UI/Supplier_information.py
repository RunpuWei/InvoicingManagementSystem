# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supplier_information.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1026, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/supplier_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("QHeaderView::section {background-color:#008CBA ; /* 蓝色 */\n"
"                                                                color: WHITE;\n"
"                                                                };\n"
"                                                                text-align : center;")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
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
        self.supplierid_supplier_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.supplierid_supplier_2.setObjectName("supplierid_supplier_2")
        self.horizontalLayout_14.addWidget(self.supplierid_supplier_2)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_14.addWidget(self.label_41)
        self.name_supplier_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.name_supplier_2.setObjectName("name_supplier_2")
        self.horizontalLayout_14.addWidget(self.name_supplier_2)
        self.search_supplier_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.search_supplier_2.setMinimumSize(QtCore.QSize(0, 30))
        self.search_supplier_2.setObjectName("search_supplier_2")
        self.horizontalLayout_14.addWidget(self.search_supplier_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.table_supplier_2 = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_supplier_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_supplier_2.setObjectName("table_supplier_2")
        self.table_supplier_2.setColumnCount(6)
        self.table_supplier_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_supplier_2.setHorizontalHeaderItem(5, item)
        self.verticalLayout_9.addWidget(self.table_supplier_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)
        mainWindow.setCentralWidget(self.centralwidget)
        self.Current_user = QtWidgets.QAction(mainWindow)
        self.Current_user.setEnabled(False)
        self.Current_user.setObjectName("Current_user")
        self.Current_department = QtWidgets.QAction(mainWindow)
        self.Current_department.setEnabled(False)
        self.Current_department.setObjectName("Current_department")
        self.exit = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resource/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon1)
        self.exit.setVisible(True)
        self.exit.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.exit.setObjectName("exit")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "供应商选择"))
        self.label_39.setText(_translate("mainWindow", "供应商信息"))
        self.label_40.setText(_translate("mainWindow", "供应商编号："))
        self.label_41.setText(_translate("mainWindow", "供应商名称:"))
        self.search_supplier_2.setText(_translate("mainWindow", "搜索"))
        item = self.table_supplier_2.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "供应商编号"))
        item = self.table_supplier_2.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "供应商姓名"))
        item = self.table_supplier_2.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "供应商联系人"))
        item = self.table_supplier_2.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "联系人电话"))
        item = self.table_supplier_2.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "供应商地址"))
        item = self.table_supplier_2.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "操作"))
        self.Current_user.setText(_translate("mainWindow", "当前用户：xxxxx"))
        self.Current_user.setToolTip(_translate("mainWindow", "当前用户：xxxxx"))
        self.Current_department.setText(_translate("mainWindow", "当前部门：xxxxx"))
        self.exit.setText(_translate("mainWindow", "退出"))

import main_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

