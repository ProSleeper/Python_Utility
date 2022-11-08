import cv2
import numpy as np
import os
import imghdr

class FileConverter:

    def resizeAndConvert(self, path):
        if(not imghdr.what(path)):  # 
            return

        BACKGROUND_SIZE = (1080, 1080)
        ALBUM_SIZE = (1920, 1920)

        BACKGROUND_FILE_NAME = "배경.png"
        ALBUM_FILE_NAME = "앨범.png"

        resizeImageList = list()
        reverseItemPath = path.rfind("\\")
        reverseItemPath = path[0:reverseItemPath+1]
        
        img_array = np.fromfile(path, np.uint8)
        src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
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

    def runMethod(self, path):
        if(os.path.isdir(path)):

            # os.walk(path) 경로를 입력하면 재귀적으로 모든 폴더와 파일을 읽는다.
            # 폴더면 directories로 파일이면 files로 자동으로 나눠준다. 쩐다....
            for (root, directories, files) in os.walk(path):    
                # for d in directories:
                #     d_path = os.path.join(root, d)
                #     print(d_path)
                for file in files:
                    file_path = os.path.join(root, file)
                    self.resizeAndConvert(file_path)
                    print(file_path)
        else:
            pass
