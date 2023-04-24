# 파일 4개로 나눈 것들의 원본!
import sys
from PyQt5 import QtWidgets
from MainWindow import MainWidget

 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWidget()
    MainWindow.show()
    sys.exit(app.exec_())