#-*- coding: euc-kr -*-

from pytube import YouTube

class LMDDownloader:
    def __init__(self, url:str, save_dir:str):
        self.url = url;
        self.save_dir = save_dir;
        self.yt = YouTube(self.url);
        self.trim_title = self.__Trim_Title();
        
    def Download(self):
        # download가 완료 되면 다운로드한 file path를 리턴해준다.
        down_path = self.yt.streams.filter(only_audio=True).first().download(output_path = self.save_dir, filename = self.trim_title)
        return self.yt.title, down_path;
        
    def __Trim_Title(self):
        return f"{self.yt.title.replace(' ', '')}.mp4";