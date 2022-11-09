import sys
from FileDragAndDropPlain import FileDragAndDropPlain
from ConvertButton import ConvertButton
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

# QMainWindow 상속받은 윈도우창이다.
class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        # 클래스로 만들어 둔 텍스트에디터와 버튼을 현재의 window에 추가시키기 위한 코드
        plain = FileDragAndDropPlain(self)
        ConvertButton(self, plain);

        self.setWindowTitle('likeMusicConverter')
        self.setFixedSize(500, 400)
        self.center();
        self.show()

    # 창 가운데 정렬을 위한 메서드
    def center(self):
        qr = self.frameGeometry()   # self(여기서는 QMainWindow)의 GeoMetry() 정보를 불러와 동일한 정보의 가상의 사각형을 생성합니다.
        cp = QDesktopWidget().availableGeometry().center() # 화면의 중앙 좌표를 계산합니다.
        qr.moveCenter(cp)   # 사각형을 중앙으로 이동합니다.
        self.move(qr.topLeft()) # 사각형을 그리는 시작지점을 왼쪽 위로 이동(즉 자신의 가로/2 세로/2 만큼씩 뺀다고 보면 된다.)
        
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWidget()
    MainWindow.show()
    sys.exit(app.exec_())