import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from UI import login
from func.ManagerFuc import selectManagerByAccount
import user.purchasing_win as purchasing
import user.sale_win as sale
import user.warehouse_win as warehouse


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)

        # 移除标题栏
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 阴影效果
        self.shadow = self.set_drop_shadow()

        # SET DROP SHADOW EFFECT IN FRAME
        self.ui.frame_Shadow.setGraphicsEffect(self.shadow)

        # SET MOVE WINDOW
        def move_window(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.drag_pos)
                self.drag_pos = event.globalPos()
                event.accept()

        # ENABLE MOUSE MOVE FORM
        self.ui.frame_TopBar.mouseMoveEvent = move_window
        # self.ui.frame_Shadow.mouseMoveEvent = move_window

        self.ui.pushButton_Exit.clicked.connect(self.click_exit)
        self.ui.pushButton_Login.clicked.connect(self.slotLogin)

    def set_drop_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        return self.shadow

    def click_exit(self):
        print("按下了关闭按钮")
        self.close()

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.slotLogin()

    def findPwd(self):
        OK = QMessageBox.warning(self, "提示", """功能待开发！""")

    # 返回登录的槽函数（目前没用）
    def BackLoginSlot(self):
        reply = QMessageBox.question(self, '退出', '确定退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('退出')
            self.MainWindow.close()
            self.show()
        else:
            print('不退出')

    def slotLogin(self):
        # 获得登录输入
        account = self.ui.lineEdit_Login.text()
        pwd = self.ui.lineEdit_Password.text()
        identity = self.ui.comboBox_department.currentIndex()  # 获取下标
        if account != '' and pwd != '':
            manage = selectManagerByAccount(account)
            if manage is not None:
                if identity == 0:  # 销售部门
                    if manage[0].getPassword() == pwd and (
                            manage[0].getDepartment() == "销售部门" or manage[0].getDepartment() == "超级管理员"):
                        self.MainWindow = QtWidgets.QMainWindow()
                        self.ui1 = sale.InvoiceSystem(self.MainWindow, manage[0])
                        self.ui1.exit.triggered.connect(self.BackLoginSlot)
                        self.MainWindow.show()
                        self.close()
                    else:
                        OK = QMessageBox.warning(self, "警告", """账号或密码错误！""")

                elif identity == 1:  # 仓库部门
                    if manage[0].getPassword() == pwd and (
                            manage[0].getDepartment() == "仓库部门" or manage[0].getDepartment() == "超级管理员"):
                        self.MainWindow = QtWidgets.QMainWindow()
                        self.ui1 = warehouse.InvoiceSystem(self.MainWindow, manage[0])
                        self.ui1.exit.triggered.connect(self.BackLoginSlot)
                        self.MainWindow.show()
                        self.close()
                    else:
                        OK = QMessageBox.warning(self, "警告", """账号或密码错误！""")

                elif identity == 2:  # 采购部门
                    if manage[0].getPassword() == pwd and (
                            manage[0].getDepartment() == "采购部门" or manage[0].getDepartment() == "超级管理员"):
                        self.MainWindow = QtWidgets.QMainWindow()
                        self.ui1 = purchasing.InvoiceSystem(self.MainWindow, manage[0])
                        self.ui1.exit.triggered.connect(self.BackLoginSlot)
                        self.MainWindow.show()
                        self.close()
                    else:
                        OK = QMessageBox.warning(self, "警告", "账号或密码错误！")
            else:
                OK = QMessageBox.warning(self, "警告", """账号不存在！""")
        else:
            OK = QMessageBox.warning(self, "警告", """账号/密码为空！""")
        # cursor.close()
        # conn.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Login()
    my.show()
    sys.exit(app.exec_())
