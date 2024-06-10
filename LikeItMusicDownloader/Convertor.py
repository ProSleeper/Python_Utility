#-*- coding: euc-kr -*-

import os
from moviepy.editor import AudioFileClip

class LMDConvertor:
    def __init__(self, title:str, read_path:str, save_path:str = None):
        self.title = title
        self.read_path = read_path
        self.save_path = save_path
        if not self.save_path:
            self.save_path = self.__Make_Save_Path()
        
    def Convert(self):
        audio = AudioFileClip(self.read_path, buffersize=13_230_000, fps=48000)
        audio.write_audiofile(self.save_path, verbose=False, logger=None, bitrate="320k")
        audio.close()
        os.remove(self.read_path) # 이 부분에서 다른 프로세스가 파일 사용 중이라서 삭제가 안된다고 나온다. 아마도 ffmpeg변환할때 subprocess를 실행시키는 코드가 있었는데 그 부분이 계속 파일을 실행시키는데 도중에 삭제하려고 해서 문제인 것 같다. 나중에 해결하자.
    
    # 당장은 뭔가 ffmpeg를 사용해서 변환할때 경로 문제가 발생한다. 이유를 잘 모르겠다.
    def __Make_Save_Path(self):
        dir_index = self.read_path.rfind(os.sep)
        read_dir = self.read_path[:dir_index]
        if read_dir.find(os.sep) == -1:
            read_dir = os.path.join(read_dir, os.sep)
        return os.path.join(read_dir, f"{self.title}.mp3")