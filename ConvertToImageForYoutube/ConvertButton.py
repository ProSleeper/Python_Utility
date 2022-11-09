
from FileConvert import FileConverter
from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton

# # QPushButton를 상속받은 버튼
class ConvertButton(QPushButton):
    def __init__(self, window, plain):  # 버튼을 누르면 plainText에 있는 path를 읽기 위해서 plain객체를 생성자 인자로 넣어준다.
        super(QPushButton, self).__init__(window)
        self.setText("변환")    # 버튼 이름
        self.move(350, 50)
        self.setFixedSize(100, 30)  # 고정된 크기
        self.plain = plain  # java에서 this.number = number 처럼 생성자에서 해주는 일

    # 마우스 up 일때 실행되는 함수 다운, 이동, 더블클릭 모두 존재한다.
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        path = self.plain.toPlainText().replace("file:///", "");    # 클릭하면 textedit에 있는 경로를 읽어서 앞의 file:///를 제거 후 path로 저장
        FileConverter().recursiveFileReading(path);    # 파일 변환을 위해서 해당 객체를 가져와서 필요한 메서드를 실행한다.
        return super().mouseReleaseEvent(e)