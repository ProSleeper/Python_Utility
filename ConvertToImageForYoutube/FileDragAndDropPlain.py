import urllib.parse
from PyQt5 import QtWidgets, QtCore


# QTextEdit을 상속받은 폴더&파일을 드래그&드롭가능한 텍스트창
class FileDragAndDropPlain(QtWidgets.QTextEdit):
    def __init__(self, window):
        super(QtWidgets.QTextEdit, self).__init__(window)
        # self.setAcceptDrops(True);    # 이걸 PyQt5에서는 이 메서드를 실행시켜야 Drop이 가능한 ui가 있다. 다만 이 QTextEdit은 기본 설정이 drop가능이고 해당 drop을 컨트롤 하기 위해서는 아래 insertFromMimeData 메서드를 오버라이딩만 해주면 된다.
        
        self.move(50, 50)       # 화면의 x,y 50만큼씩 이동(기준 왼쪽 위)
        self.setFixedSize(280, 180)   # 고정 사이즈

    # QTextEdit의 메서드 오버라이드
    # 폴더&파일을 해당 text창에 드롭하면 실행된다.
    def insertFromMimeData(self, source: QtCore.QMimeData) -> None:
        path = urllib.parse.unquote(source.text())
        self.setText(path)
