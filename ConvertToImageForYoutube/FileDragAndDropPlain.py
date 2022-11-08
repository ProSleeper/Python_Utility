import urllib.parse
from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtCore

# QTextEdit을 상속받은 폴더&파일을 드래그&드롭가능한 텍스트창
class FileDragAndDropPlain(QTextEdit):
    def __init__(self, window):
        super(QTextEdit, self).__init__(window)
        self.setAcceptDrops(True);
        self.move(50, 50)       # 화면의 x,y 50만큼씩 이동(기준 왼쪽 위)
        self.setFixedSize(280, 180)   # 고정 사이즈

    # QTextEdit의 메서드 오버라이드
    # 폴더&파일을 해당 text창에 드롭하면 실행된다.
    def insertFromMimeData(self, source: QtCore.QMimeData) -> None:
        path = urllib.parse.unquote(source.text())
        self.setText(path)
