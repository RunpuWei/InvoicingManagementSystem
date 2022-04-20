import sys

from PyQt5.QtWidgets import QApplication, QWidget
from UI.outboundinfo_widget import Ui_Form   #导入py文件中的类


class win(QWidget,Ui_Form):  #继承类

    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setupUi(self)   #执行类中的setupUi函数

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())