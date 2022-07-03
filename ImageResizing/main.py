import cv2
import glob
import numpy as np
import os

# 유튜브 올리는 노래의 앨범커버 크기를 변환하려고 만든 코드
# 역시 파이썬은 대단히 간단하네;
# 여기서 더 추가하자면 유튜브 동영상 추가처럼 마우스로 끌어와서 변환시키는 정도만 추가하면 괜찮을듯?
# 아니면 윈도우 창을 띄워서 마우스로 끌어와서 추가하면 자동으로 원래 있던 폴더에 해주는 것도 괜찮고

imageList = glob.glob('C:\\Users\\ingn\\Documents\\LIKEITMUSIC\\7월\\##############작업할 노래\\**\\*.jpg', recursive = True)

for item in imageList:
    resizeImageList = list()
    reverseItemPath = item.rfind("\\")
    reverseItemPath = item[0:reverseItemPath+1]
    
    img_array = np.fromfile(item, np.uint8)
    src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    resizeImageList.append(cv2.resize(src, dsize=(1080, 1080), interpolation=cv2.INTER_LINEAR))
    resizeImageList.append(cv2.resize(src, dsize=(1920, 1920), interpolation=cv2.INTER_LINEAR))
    
    imageName = ["앨범.png", "배경.png"]
    imageName[0] = reverseItemPath + imageName[0]
    imageName[1] = reverseItemPath + imageName[1]
    extension = os.path.basename(".png") # 이미지 확장자
    
    for iter in range(0, len(resizeImageList)):
        result, encoded_img = cv2.imencode(extension, resizeImageList[iter])
    
        if result:
            with open(imageName[iter], mode='w+b') as f:
                encoded_img.tofile(f)
    
