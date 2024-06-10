#-*- coding: euc-kr -*-

import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QMouseEvent
from Executor import LMDExecutor

class CreateApp():
    def __init__(self):
        self.app = QApplication([])
        MainWindow = MainWidget()
        self.app.exec_()
        
# QMainWindow 상속받은 윈도우창이다.
class MainWidget(QMainWindow):
    def __init__(self):
        # super(MainWidget, self).__init__(parent)
        super(MainWidget, self).__init__()

        # 클래스로 만들어 둔 텍스트에디터와 버튼을 현재의 window에 추가시키기 위한 코드
        line_edit_list = []
        for offset in range(10):
            line_edit_list.append(UrlTextLineEdit(self, offset))
        ConvertButton(self, line_edit_list)

        self.setWindowTitle('likeMusicConverter')
        # self.setWindowFlags(Qt.WindowStaysOnTopHint) # 다른 파일을 드롭 시키는 프로그램이라서 always on top 설정
        self.setFixedSize(500, 400)
        self.center()
        self.show()
        
    # 창 가운데 정렬을 위한 메서드
    def center(self):
        qr = self.frameGeometry()   # self(여기서는 QMainWindow)의 GeoMetry() 정보를 불러와 동일한 정보의 가상의 사각형을 생성합니다.
        cp = QDesktopWidget().availableGeometry().center() # 화면의 중앙 좌표를 계산합니다.
        qr.moveCenter(cp)   # 사각형을 중앙으로 이동합니다.
        self.move(qr.left() + qr.width() / 1.5, qr.top()) # 항상 다른 파일을 드롭 시켜야 하니까 중앙보다는 약간 옆에 좋은 듯 해서. 일단 먼저 center로 두고 가로를 왼쪽 기준으로 창 크기의 2/3만큼 오른쪽으로 이동 시켰고, 세로 위치는 동일하게.

# QTextEdit을 상속받은 폴더&파일을 드래그&드롭가능한 텍스트창
class UrlTextLineEdit(QLineEdit):
    def __init__(self, window, offset:int):
        super(QLineEdit, self).__init__(window)
        # self.setAcceptDrops(True);    # 이걸 PyQt5에서는 이 메서드를 실행시켜야 Drop이 가능한 ui가 있다. 다만 이 QTextEdit은 기본 설정이 drop가능이고 해당 drop을 컨트롤 하기 위해서는 아래 insertFromMimeData 메서드를 오버라이딩만 해주면 된다.
        self.move(50, 50 + offset * 25)       # 화면의 x,y 50만큼씩 이동(기준 왼쪽 위)
        self.setFixedSize(280, 20)   # 고정 사이즈
        
# QPushButton를 상속받은 버튼
class ConvertButton(QPushButton):
    def __init__(self, window, line_edit_list:list):  # 버튼을 누르면 plainText에 있는 path를 읽기 위해서 plain객체를 생성자 인자로 넣어준다.
        super(QPushButton, self).__init__(window)
        self.setText("다운로드")    # 버튼 이름
        self.move(350, 50)
        self.setFixedSize(100, 30)  # 고정된 크기
        self.line_edit_list = line_edit_list  # java에서 this.number = number 처럼 생성자에서 해주는 일

    # 마우스 up 일때 실행되는 함수 다운, 이동, 더블클릭 모두 존재한다.
    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if len(self.line_edit_list) == 0:
            return;
        
        url_list = [line_edit.text() for line_edit in self.line_edit_list ]
        save_dir = "C:\\Users\\ingn\\Documents\\LIKEITMUSIC\\##############작업할 노래1"
        downloader = LMDExecutor(url_list, save_dir)
        downloader.DownLoad()
        time.sleep(1.5)
        # 다운로드 기능 실행.
        # FileConverter().runPathList(self.plain.path_list)
        
        for line_edit in self.line_edit_list:
            line_edit.setText("")
        QMessageBox.information(self, "Info", "다운로드 완료.", QMessageBox.Ok)
        return super().mouseReleaseEvent(e)
    
