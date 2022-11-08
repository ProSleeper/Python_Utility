# 파일 4개로 나눈 것들의 원본!

import cv2
import numpy as np
import os
import sys
import imghdr
import urllib.parse
from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget


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

# # QPushButton를 상속받은 버튼
class ConvertButton(QPushButton):
    def __init__(self, window, plain):  # 버튼을 누르면 plainText에 있는 path를 읽기 위해서 plain객체를 생성자 인자로 넣어준다.
        super(QPushButton, self).__init__(window)
        self.setText("변환")    # 버튼 이름
        self.move(350, 50)
        self.setFixedSize(100, 30)
        self.plain = plain  # java에서 this.number = number 처럼 생성자에서 해주는 일

    # 마우스 up 일때 실행되는 함수 다운, 이동, 더블클릭 모두 존재한다.
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        path = self.plain.toPlainText().replace("file:///", "");    # 클릭하면 textedit에 있는 경로를 읽어서 앞의 file:///를 제거 후 path로 저장
        runMethod(path)
        return super().mouseReleaseEvent(e)

def resizeAndConvert(path):
    if(not imghdr.what(path)):  # 
        return

    BACKGROUND_SIZE = (1080, 1080)
    ALBUM_SIZE = (1920, 1920)

    BACKGROUND_FILE_NAME = "배경.png"
    ALBUM_FILE_NAME = "앨범.png"

    resizeImageList = list()
    reverseItemPath = path.rfind("\\")
    reverseItemPath = path[0:reverseItemPath+1]
    
    img_array = np.fromfile(path, np.uint8)
    src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    resizeImageList.append(cv2.resize(src, dsize=BACKGROUND_SIZE, interpolation=cv2.INTER_LINEAR))
    resizeImageList.append(cv2.resize(src, dsize=ALBUM_SIZE, interpolation=cv2.INTER_LINEAR))
    
    imageName = []
    imageName.append(reverseItemPath + ALBUM_FILE_NAME)
    imageName.append(reverseItemPath + BACKGROUND_FILE_NAME)
    extension = os.path.basename(".png") # 이미지 확장자
    
    for iter in range(0, len(resizeImageList)):
        result, encoded_img = cv2.imencode(extension, resizeImageList[iter])
    
        if result:
            with open(imageName[iter], mode='w+b') as f:
                encoded_img.tofile(f)

def runMethod(path):
    if(os.path.isdir(path)):

        # os.walk(path) 경로를 입력하면 재귀적으로 모든 폴더와 파일을 읽는다.
        # 폴더면 directories로 파일이면 files로 자동으로 나눠준다. 쩐다....
        for (root, directories, files) in os.walk(path):    
            # for d in directories:
            #     d_path = os.path.join(root, d)
            #     print(d_path)
            for file in files:
                file_path = os.path.join(root, file)
                resizeAndConvert(file_path)
                print(file_path)
    else:
        pass


# QMainWindow 상속받은 윈도우창이다.
class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        plain = FileDragAndDropPlain(self)
        button = ConvertButton(self, plain);

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