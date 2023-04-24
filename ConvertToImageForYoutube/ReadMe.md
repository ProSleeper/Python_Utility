# ConvertToImageForYoutube
## ��Ʃ�� ä�ο� ���� �ø� �� �� �̹��� �ڵ� ��ȯ
- ��� �̹��� ������ ���(1920x1920)�� �ٹ�(1080x1080) �ػ󵵿� PNG ���Ϸ� ��ȯ���ش�.
- ~~���� ���� �� build ��ɾ� >> python setup.py build~~
- build ��ɾ� >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2
dependency: urllib.parse, PyQt5, cv2, numpy, imghdr

## Run Environment
OS: window 10

## Version History
### v.20221231
- ���� 1�� Ȥ�� ���� 1�� ���� ��� ������ ��ȯ ����.
### v.20230414
- �ټ��� ������ �ѹ��� �巡��&����ص� ��� ��ȯ ����.
- ~~���� 2�� �̻� ���� �巡��&��� �� ���� �߻�. ���� �ذ� ��~~: �ذ�.
- ���� �� Opencv config ������ �߻��ؼ� chatGPT���� ������� �ذ��ߴ�. ���� ��Ű�� ������ ������ �����ΰ� ����.
- �׸��� pyinstaller �� ���� ��� ����.
### v.20230424
- �׻� ����(always on top) �ڵ尡 �ȸԱ淡 �� �ȸԴ��� chatGPT���� ������ ������� �ذ��� �ȵƴ�.
- �׷��� ���� �˻��� �ϰ� �������� �ߴµ��� �ȵǱ淡 �ڵ带 �ٽ� �ôµ� MainWindow.py�� main.py�� �ߺ��Ǵ� �κ��� �־���.
- �׸��� ���� ���α׷��� windowâ�� ����°� main.py���� ����µ� �� ��� MainWindow.py�� ������ �־���...
- �׷��� MainWindow.py���� windowâ�� ����� �ڵ�� ����.
- ### v.20230425
- �ڵ带 �ٽ� ���µ� UI�κ� �ڵ���� �ǹ̾��� ���Ϸθ� �������� �־ UI MainWindowUI.py ���Ϸ� ����.
- �׸��� ����� pyinstaller�� �����ϱ� ������ ������ python setup.py build �� �����Ҷ� �ʿ��ߴ� setup.py ������ ����.
