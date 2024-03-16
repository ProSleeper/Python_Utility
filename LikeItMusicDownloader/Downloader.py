#-*- coding: euc-kr -*-

from pytube import YouTube

class LMDDownloader:
    def __init__(self, url:str, save_dir:str):
        try:
            self.url = url
            self.save_dir = save_dir
            self.yt = YouTube(self.url)
            self.trim_title = self.__Trim_Title()
            
        except BaseException as e:
            print(f"[{self.__class__.__name__}], Error: {str(e)}")
        
        
    def Download(self):
        # download가 완료 되면 다운로드한 file path를 리턴해준다.
        down_path = self.yt.streams.filter(only_audio=True).first().download(output_path = self.save_dir, filename = self.trim_title)
        return self.yt.title, down_path
        
    def __Trim_Title(self):
        return f"{self.yt.title.replace(' ', '')}.mp4"