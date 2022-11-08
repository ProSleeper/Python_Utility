from cx_Freeze import setup, Executable
import sys





buildOptions = dict(packages = ["PyQt5","urllib","imghdr","numpy", "cv2", "os", "sys"],  # 1
excludes = ["scipy.spatial.cKDTree"])

exe = [Executable("MainWindow.py")]  # 2

# 3
setup(
    name= '이미지 자동 변환기',
    version = '0.5',
    author = "KYW",
    description = "유튜브 음악 업로드시 사용할 앨범 커버 자동 크기 조절",
    options = dict(build_exe = buildOptions),
    executables = exe
)