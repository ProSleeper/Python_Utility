# ConvertToImageForYoutube
## 유튜브 채널에 음악 올릴 때 쓸 이미지 자동 변환
- 모든 이미지 파일을 배경(1920x1920)과 앨범(1080x1080) 해상도와 PNG 파일로 변환해준다.
- ~~추후 수정 후 build 명령어 >> python setup.py build~~
- build 명령어 >> pyinstaller --onefile --noconsole main.py
<hr>
<br><br>

## Build Environment
build version: Python 3.8.2
dependency: urllib.parse, PyQt5, cv2, numpy, imghdr

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
### v.20230424
- 항상 위에(always on top) 코드가 안먹길래 왜 안먹는지 chatGPT한테 열심히 물어봐도 해결이 안됐다.
- 그래서 구글 검색도 하고 여러가지 했는데도 안되길래 코드를 다시 봤는데 MainWindow.py랑 main.py에 중복되는 부분이 있었다.
- 그리고 실제 프로그램의 window창을 만드는건 main.py에서 만드는데 난 계속 MainWindow.py를 만지고 있었다...
- 그래서 MainWindow.py에서 window창을 만드는 코드로 수정.
### v.20230425
- 코드를 다시 보는데 UI부분 코드들이 의미없이 파일로만 나누어져 있어서 UI MainWindowUI.py 파일로 통합.
- 그리고 현재는 pyinstaller로 빌드하기 때문에 이전에 python setup.py build 로 빌드할때 필요했던 setup.py 파일은 삭제.
### v.20230501
- 다중 폴더 경로 입력 시 버그 해결
    - 잘 되는 줄 알았는데 테스트 해보니 안되고 프로그램 문제가 있었음.
- 변환 부분 멀티 스레딩 적용.
    - 그리 많이 변환하는 것도 아닌데도, 이미지 변환이라는 작업이 무거워서 싱글 스레드 작업으로는 20개만 되어도 시간이 오래 걸려서 멀티 스레딩 구조로 변경
- 모든 작업 완료 시 알림창 뜨도록 변경.
- 원래는 멀티 스레딩을 적용하는 것도 depth1 정도, 즉 하나의 함수나 범위에서 멀티 스레딩을 적용하려고 했으나 입력되는 부분이 2가지라서(1개의 폴더에서 하위 폴더로 나눠지는 구조1, 여러개의 폴더에서 하위 폴더로 나눠지는 구조2) 어쩔 수 없이 depth2정도의 스레드 구조(스레드에서 또 하위 스레드 생성)로 작성.
- 시간 확인하는 코드는 Util.py로 이동
