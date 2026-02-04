#!/usr/bin/env python3
import sys
import os

# OS 판별: 윈도우면 GUI, 리눅스면 CLI
if os.name == 'nt' or sys.platform.startswith('win'):  # Windows
    from MainWindowUI import CreateApp
    if __name__ == "__main__":
        CreateApp()
else:  # Linux/CLI 모드
    from FileConvert import FileConverter
    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("How to Use: ./main <path1> [path2 ...]")
            print("example: ./main /path/to/folder1 /path/to/image.jpg")
            sys.exit(1)

        paths = sys.argv[1:]
        converter = FileConverter()
        converter.runPathList(paths)
        print("Complete to Convert!")
