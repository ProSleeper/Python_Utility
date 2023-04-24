from cx_Freeze import setup, Executable

# 스프링에 빗대서 설명하자면 의존성 추가라고 보면 된다. 내가 만든 프로그램에서 사용했던 library들을 전부 같이 빌드한다는 옵션이다.
buildOptions = dict(packages = ["PyQt5","urllib","imghdr","numpy", "cv2", "os", "sys"],  # 1
excludes = ["scipy.spatial.cKDTree"])   # 현재 나는 사용하지 않는 library인데 복붙 하다보니까 들어갔다. 예시로 남겨두자. 여기에 작성하면 해당 library는 빌드에서 제외시킨다.

exe = [Executable("MainWindow.py", base="Win32GUI")]  # 2   base="Win32GUI" 를 작성해줘야 프로그램 실행 시 console창이 뜨지 않는다.

# 3
setup(
    name= '이미지 자동 변환기',
    version = '0.5',
    author = "KYW",
    description = "유튜브 음악 업로드시 사용할 앨범 커버 자동 크기 조절",
    options = dict(build_exe = buildOptions),
    executables = exe
)

# 빌드 명령어 python setup.py build