# LikeItMusic Downloader
## 

## ��Ʃ�� ������ �ּҸ� ������� ���� �ٿ�ε�
- ��Ʃ�� �������� �˻� �� ���� url�� ������ �ٿ�ε�
- pytube ���� �ٿ� �޴µ� .mp3���Ϸ� �ٷ� �ٿ��� �Ұ����ؼ� .mp4�� �ٿ�ε� �� moviepy ���� Hz�� bitrate�� ������ .mp3�� ��ȯ ��Ų��. 
- build ��ɾ� >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2
dependency: pytube, moviepy

## Run Environment
OS: window 10

## Version History
### v.20231015
- ��� �������� �ϴ� ������ ������ �־�� youtube �ٿ� �ڵ常 �׽�Ʈ �غ��ٰ� �ð��� �����ż� �ٽ� �������� �׽�Ʈ�� �ϰ� ���� ���� ������ �ٿ� -> mp3 ��ȯ �ڵ常 �����ߴ�.
- �׸��� �ּҸ� �Է��ϸ� �ٿ�޴� ���·� �ؾ��ؼ� ui�� ������ �Ұ� ���Ƽ� �̹��� ��ȯ �ڵ常 ctfy_src�� �����صξ���.
### v.20231017
- �� �ǳ� �׽�Ʈ �� �ٿ�޾ƺôµ� "pytube.exceptions.AgeRestrictedError: Q2x7i5xk2ZY is age restricted, and can't be accessed without logging in." �̷��� ������ �߻��ؼ� �˻��غ��� ���������� �ִ� ������� �׷��ٴ� ���� ������ ��� �ذ��ؾ��ϳ� ã�ٰ� �߰��ߴ�.
- ���� �� window ��Ű�� ����� C:\Python\Python38-32\Lib\site-packages\pytube\innertube.py���Ͽ��� 223���� ANDROID_MUSIC�� ANDROID�� �����ϸ� �ٿ��� �ȴٴ� stackoverflow �亯�� �־ �����غôµ� ���� �ȴ�. �� �׷����� �� �� ������.. �ϴ� �Ǵϱ� �ش� �κп� �ּ��� �޾Ƴ��� �����ߴ�.
- ���� �� �ٿ�ε�� �� �Ǵµ� �Ʒ�ó�� ������ �߻��ߴ�.
- �Ƹ��� os.remove(self.read_path) �� �κп��� �ٸ� ���μ����� ���� ��� ���̶� ������ �ȵǴ� �� ����. �Ƹ��� ffmpeg��ȯ�Ҷ� subprocess�� �����Ű�� �ڵ尡 �־��µ� �� �κ��� ���� ���� ���� ���ε�, �����Ϸ��� �ؼ� ������ �� ����. ���߿� �ذ�����.
    ```python
            Traceback (most recent call last):
        File ".\main.py", line 61, in <module>
            os.remove(read_path)
        PermissionError: [WinError 32] �ٸ� ���μ����� ������ ��� ���̱� ������ ���μ����� �׼��� �� �� �����ϴ�: 'C:\\Users\\ingn\\Documents\\python\\Python_Utility\\LikeItMusicDownloader\\Worse.mp4'
    ```
- �� �ܿ� ����̳� �ڵ� ������ ����.
