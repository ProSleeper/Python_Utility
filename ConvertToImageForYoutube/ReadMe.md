# ConvertToImageForYoutube
## 유튜브 채널에 음악 올릴 때 쓸 이미지 자동 변환
- 모든 이미지 파일을 배경(1920x1920)과 앨범(1080x1080) 해상도와 PNG 파일로 변환해준다.
- ~~추후 수정 후 build 명령어 >> python setup.py build~~
- build 명령어 >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2

## Run Environment
OS: window 10

## Version History
### v.20221231
- 폴더 1개 혹은 폴더 1개 하위 모든 폴더의 변환 지원.
### v.20230414
- 다수의 폴더를 한번에 드래그&드롭해도 모두 변환 지원.
- ~~현재 2개 이상 폴더 드래그&드롭 시 에러 발생. 문제 해결 중~~: 해결.
- 빌드 후 Opencv config 에러가 발생해서 chatGPT한테 물어봐서 해결했다. 뭔가 패키지 버전과 의존성 문제인것 같다.
- 그리고 pyinstaller 로 빌드 방식 변경.
