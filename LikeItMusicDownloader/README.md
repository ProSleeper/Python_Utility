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