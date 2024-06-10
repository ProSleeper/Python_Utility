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
        
# QMainWindow ��ӹ��� ������â�̴�.
class MainWidget(QMainWindow):
    def __init__(self):
        # super(MainWidget, self).__init__(parent)
        super(MainWidget, self).__init__()

        # Ŭ������ ����� �� �ؽ�Ʈ�����Ϳ� ��ư�� ������ window�� �߰���Ű�� ���� �ڵ�
        line_edit_list = []
        for offset in range(10):
            line_edit_list.append(UrlTextLineEdit(self, offset))
        ConvertButton(self, line_edit_list)

        self.setWindowTitle('likeMusicConverter')
        # self.setWindowFlags(Qt.WindowStaysOnTopHint) # �ٸ� ������ ��� ��Ű�� ���α׷��̶� always on top ����
        self.setFixedSize(500, 400)
        self.center()
        self.show()
        
    # â ��� ������ ���� �޼���
    def center(self):
        qr = self.frameGeometry()   # self(���⼭�� QMainWindow)�� GeoMetry() ������ �ҷ��� ������ ������ ������ �簢���� �����մϴ�.
        cp = QDesktopWidget().availableGeometry().center() # ȭ���� �߾� ��ǥ�� ����մϴ�.
        qr.moveCenter(cp)   # �簢���� �߾����� �̵��մϴ�.
        self.move(qr.left() + qr.width() / 1.5, qr.top()) # �׻� �ٸ� ������ ��� ���Ѿ� �ϴϱ� �߾Ӻ��ٴ� �ణ ���� ���� �� �ؼ�. �ϴ� ���� center�� �ΰ� ���θ� ���� �������� â ũ���� 2/3��ŭ ���������� �̵� ���װ�, ���� ��ġ�� �����ϰ�.

# QTextEdit�� ��ӹ��� ����&������ �巡��&��Ӱ����� �ؽ�Ʈâ
class UrlTextLineEdit(QLineEdit):
    def __init__(self, window, offset:int):
        super(QLineEdit, self).__init__(window)
        # self.setAcceptDrops(True);    # �̰� PyQt5������ �� �޼��带 ������Ѿ� Drop�� ������ ui�� �ִ�. �ٸ� �� QTextEdit�� �⺻ ������ drop�����̰� �ش� drop�� ��Ʈ�� �ϱ� ���ؼ��� �Ʒ� insertFromMimeData �޼��带 �������̵��� ���ָ� �ȴ�.
        self.move(50, 50 + offset * 25)       # ȭ���� x,y 50��ŭ�� �̵�(���� ���� ��)
        self.setFixedSize(280, 20)   # ���� ������
        
# QPushButton�� ��ӹ��� ��ư
class ConvertButton(QPushButton):
    def __init__(self, window, line_edit_list:list):  # ��ư�� ������ plainText�� �ִ� path�� �б� ���ؼ� plain��ü�� ������ ���ڷ� �־��ش�.
        super(QPushButton, self).__init__(window)
        self.setText("�ٿ�ε�")    # ��ư �̸�
        self.move(350, 50)
        self.setFixedSize(100, 30)  # ������ ũ��
        self.line_edit_list = line_edit_list  # java���� this.number = number ó�� �����ڿ��� ���ִ� ��

    # ���콺 up �϶� ����Ǵ� �Լ� �ٿ�, �̵�, ����Ŭ�� ��� �����Ѵ�.
    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if len(self.line_edit_list) == 0:
            return;
        
        url_list = [line_edit.text() for line_edit in self.line_edit_list ]
        save_dir = "C:\\Users\\ingn\\Documents\\LIKEITMUSIC\\##############�۾��� �뷡1"
        downloader = LMDExecutor(url_list, save_dir)
        downloader.DownLoad()
        time.sleep(1.5)
        # �ٿ�ε� ��� ����.
        # FileConverter().runPathList(self.plain.path_list)
        
        for line_edit in self.line_edit_list:
            line_edit.setText("")
        QMessageBox.information(self, "Info", "�ٿ�ε� �Ϸ�.", QMessageBox.Ok)
        return super().mouseReleaseEvent(e)
    
