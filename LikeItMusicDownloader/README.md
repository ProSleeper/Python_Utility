# LikeItMusic Downloader
## 

## 유튜브 뮤직의 주소를 기반으로 음악 다운로드
- 유튜브 뮤직에서 검색 후 공유 url로 음악을 다운로드
- pytube 모듈로 다운 받는데 .mp3파일로 바로 다운이 불가능해서 .mp4로 다운로드 후 moviepy 모듈로 Hz와 bitrate를 높여서 .mp3로 변환 시킨다. 
- build 명령어 >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2, pyinstaller 6.1.0
dependency: PyQt5, pytube, moviepy

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
### v.20231029
- 기존에 만든 이미지 변환 프로젝트에서 ui부분만 코드 수정해서 10개의 url음악을 한번에 다운 받을 수 있도록 기능 추가.
- log, config등 하려면 할 기능이 너무나 많지만, 내가 사용하려는 기능이 제일 우선이므로 간단하게 ui추가하고 다운로드 경로는 고정시켜서 구현함.
- 현재는 코드가 전부 동기적이라서 10개의 곡을 한번에 다운받으면 꽤 시간이 걸릴텐데 추후 스레드 적용해서 병렬로 처리하자.(아 이번에는 비동기로 구현해볼까? 어차피 오래 걸리는 부분은 io니까)
- 이미지 변환기와 마찬가지로 build 시켜서 먼저 사용하는 게 목적이라서 일단 여기까지!
- pyinstaller로 빌드하려고 했는데 계속 utf-8 UTFEncodingError 라고 뜨길래 코드가 euc-kr이라서 그런줄 알고 이것저것 바꿔보고 검색도 해봤는데, 거의 다 안됐었다.
- 다행이 stackoverflow에서 힌트를 얻어서 pyinstaller가 문제일 수도 있다는 생각이 들어서 최신버전 5.10.1 -> 6.1.0 으로 업데이트 후 실행하니까 오류없이 됐다.
- 다만 변환할때 ffmpeg가 필요하다보니 실행파일의 크기가 100mb가 넘어간다. 아마도 ffmpeg파일의 크기만 77mb가 되어서 그런거 같다.

### v.20231029
- 빌드후 사용하던 프로그램이 갑자기 작동이 제대로 되지 않았다.
- 빌드 한 프로그램이니 당연히 건드릴 것도, 건드린 것도 없는데 약간 어처구니가 없었다.
- 몇번 검색하니 pytube 자체의 오류라고 하는 것 같다.
- 그래서 pytube를 재설치하거나 기존 pytube를 삭제하고 pytube3를 설치하라고 해서 먼저 pytube3를 설치해서 해봤는데 안됐다.
- 그래서 pytube만 재설치 후 실행하니까 되어서 그냥 바로 재빌드하고 사용하기로 했다.

- 재설치 후 실행하니 한번은 다운로드가 됐는데 다시 하니 안되고 해결을 못했다.
- 시간이 날때 다른 방법으로 해결해보자.
- 다른 방법이란.. 아마 다른 패키지를 사용해야 될 것 같다