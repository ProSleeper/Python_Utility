# LikeItMusic Downloader
## 

## 유튜브 뮤직의 주소를 기반으로 음악 다운로드
- 유튜브 뮤직에서 검색 후 공유 url로 음악을 다운로드
- pytube 모듈로 다운 받는데 .mp3파일로 바로 다운이 불가능해서 .mp4로 다운로드 후 moviepy 모듈로 Hz와 bitrate를 높여서 .mp3로 변환 시킨다. 
- build 명령어 >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2
dependency: pytube, moviepy

## Run Environment
OS: window 10

## Version History
### v.20231015
- 계속 만들어야지 하던 생각만 가지고 있었어서 youtube 다운 코드만 테스트 해보다가 시간이 오래돼서 다시 여러가지 테스트를 하고 아주 아주 간단한 다운 -> mp3 변환 코드만 구현했다.
- 그리고 주소를 입력하면 다운받는 형태로 해야해서 ui를 만들어야 할것 같아서 이미지 변환 코드만 ctfy_src에 복사해두었다.
### v.20231017
- 잘 되나 테스트 겸 다운받아봤는데 "pytube.exceptions.AgeRestrictedError: Q2x7i5xk2ZY is age restricted, and can't be accessed without logging in." 이렇게 에러가 발생해서 검색해보니 연령제한이 있는 동영상라서 그렇다는 말이 보여서 어떻게 해결해야하나 찾다가 발견했다.
- 현재 내 window 패키지 경로의 C:\Python\Python38-32\Lib\site-packages\pytube\innertube.py파일에서 223줄의 ANDROID_MUSIC을 ANDROID로 변경하면 다운이 된다는 stackoverflow 답변이 있어서 수정해봤는데 정말 된다. 왜 그런지는 알 수 없지만.. 일단 되니까 해당 부분에 주석을 달아놓고 수정했다.
- 수정 후 다운로드는 잘 되는데 아래처럼 오류가 발생했다.
- 아마도 os.remove(self.read_path) 이 부분에서 다른 프로세스가 파일 사용 중이라서 삭제가 안되는 것 같다. 아마도 ffmpeg변환할때 subprocess를 실행시키는 코드가 있었는데 그 부분이 아직 파일 실행 중인데, 삭제하려고 해서 문제인 것 같다. 나중에 해결하자.
    ```python
            Traceback (most recent call last):
        File ".\main.py", line 61, in <module>
            os.remove(read_path)
        PermissionError: [WinError 32] 다른 프로세스가 파일을 사용 중이기 때문에 프로세스가 액세스 할 수 없습니다: 'C:\\Users\\ingn\\Documents\\python\\Python_Utility\\LikeItMusicDownloader\\Worse.mp4'
    ```
- 그 외에 기능이나 코드 수정은 없다.
