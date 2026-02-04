import cv2
import numpy as np
import os
import imghdr
import threading
from Util import ElapsedTime


class WorkerThreads():
    def __init__(self, target_function):
        self.threads = [];
        self.target_function = target_function;
    
    def thread_add(self, arg):
        self.threads.append(threading.Thread(target=self.target_function, args=(arg,)))
    
    def thread_proc(self):
        for t in self.threads:
            t.start()
            
        for t in self.threads:
            t.join()

class FileConverter:
    def resizeAndConvert(self, path):
        if(not imghdr.what(path)):  # 해당 path에 있는 파일 혹은 폴더가(여기서는 folder는 오지 않으므로 파일만) 이미지인지 확인
            return

        BACKGROUND_SIZE = (1080, 1080)
        ALBUM_SIZE = (1920, 1920)

        BACKGROUND_FILE_NAME = "bg.png"
        ALBUM_FILE_NAME = "cover.png"

        resizeImageList = list()
        reverseItemPath = path.rfind("/")
        reverseItemPath = path[0:reverseItemPath+1]
        
        img_array = np.fromfile(path, np.uint8)
        src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        # 이미지 변환 라이브러리 cv2 를 사용한 것이고, INTER_LINEAR 말고도 다른 여러가지 알고리즘이 존재한다.
        resizeImageList.append(cv2.resize(src, dsize=BACKGROUND_SIZE, interpolation=cv2.INTER_LINEAR))
        resizeImageList.append(cv2.resize(src, dsize=ALBUM_SIZE, interpolation=cv2.INTER_LINEAR))
        
        imageName = []
        imageName.append(reverseItemPath + ALBUM_FILE_NAME)
        imageName.append(reverseItemPath + BACKGROUND_FILE_NAME)
        extension = os.path.basename(".png") # 이미지 확장자
        
        for iter in range(0, len(resizeImageList)):
            result, encoded_img = cv2.imencode(extension, resizeImageList[iter])
        
            if result:
                with open(imageName[iter], mode='w+b') as f:
                    encoded_img.tofile(f)

    def runPathList(self, path_list):
        convertTime = ElapsedTime();
        pathListThreads = WorkerThreads(self.recursiveDirectory);
        for path in path_list:
            pathListThreads.thread_add(path)
        
        pathListThreads.thread_proc();
        
        convertTime.endTime();
        
    def recursiveDirectory(self, path):
        pathThreads = WorkerThreads(self.resizeAndConvert);
        if(os.path.isdir(path)):
                # os.walk(path) 경로를 입력하면 재귀적으로 모든 폴더와 파일을 읽는다.
                # 폴더면 directories로 파일이면 files로 자동으로 나눠준다. 쩐다....
            for (root, directories, files) in os.walk(path):
                # os.walk(path)는 어떤 경로를 주면 그 하위 경로에 있는 폴더와 파일을 나눠서 재귀적으로 전부 확인한다.
                # 폴더 구조가 aaa폴더에 bbb와ccc 폴더가 존재한다면
                #          /aaa -> /bbb -> /ddd, pic.jpg
                #               -> /ccc -> /eee -> /fff, manyo.exe
                # 이런 구조라면 os.walk의 순회 순서는
                # 1. /aaa 폴더와 파일
                # 2. /bbb 폴더
                # 3. /ddd 폴더와 pic.jpg
                # 4. /ccc 폴더
                # 5. /eee 폴더
                # 6. /fff 폴더와 manyo.exe
                # 의 순서로 모든 폴더와 파일을 순회한다.
                # for d in directories:
                #     d_path = os.path.join(root, d)
                #     print(d_path)
                for file in files:
                    file_path = os.path.join(root, file).replace("\\","/")   # 파일이 현재 들어있는 path와 파일 이름을 합쳐서 file_path를 만든다.
                    # self.resizeAndConvert(file_path)    # 크기와 파일형식 변환
                    pathThreads.thread_add(file_path);
                    # print(file_path)
        else:
            # self.resizeAndConvert(path)
            pathThreads.thread_add(path);
        
        pathThreads.thread_proc();

