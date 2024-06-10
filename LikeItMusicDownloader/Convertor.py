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
        os.remove(self.read_path) # �� �κп��� �ٸ� ���μ����� ���� ��� ���̶� ������ �ȵȴٰ� ���´�. �Ƹ��� ffmpeg��ȯ�Ҷ� subprocess�� �����Ű�� �ڵ尡 �־��µ� �� �κ��� ��� ������ �����Ű�µ� ���߿� �����Ϸ��� �ؼ� ������ �� ����. ���߿� �ذ�����.
    
    # ������ ���� ffmpeg�� ����ؼ� ��ȯ�Ҷ� ��� ������ �߻��Ѵ�. ������ �� �𸣰ڴ�.
    def __Make_Save_Path(self):
        dir_index = self.read_path.rfind(os.sep)
        read_dir = self.read_path[:dir_index]
        if read_dir.find(os.sep) == -1:
            read_dir = os.path.join(read_dir, os.sep)
        return os.path.join(read_dir, f"{self.title}.mp3")