import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip


# YouTube('https://youtu.be/Rc0smU6n-vM').streams.first().download()
# 유튜브나 유튜브 뮤직 둘다 playlist를 얻을 수 있는 메서드
# pl = Playlist(
#     'https://music.youtube.com/playlist?list=OLAK5uy_nBl9St6mOl7S_8DxyvVOSVcIHm9-5nSHM&feature=shar')
# pl1 = pl[0]
# pl2 = pl[1]


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
    
class LMDConvertor:
    def __init__(self, title:str, read_path:str, save_path:str = None):
        self.title = title;
        self.read_path = read_path;
        self.save_path = save_path;
        if not self.save_path:
            self.save_path = self.__Make_Save_Path();
        
    def Convert(self):
        audio = AudioFileClip(self.read_path, buffersize=13_230_000, fps=48000)
        audio.write_audiofile(self.save_path, verbose=False, logger=None, bitrate="320k")
    
        os.remove(self.read_path)
    
    # 당장은 뭔가 ffmpeg를 사용해서 변환할때 경로 문제가 발생한다. 이유를 잘 모르겠다.
    def __Make_Save_Path(self):
        dir_index = self.read_path.rfind(os.sep)
        read_dir = self.read_path[:dir_index];
        if read_dir.find(os.sep) == -1:
            read_dir = os.path.join(read_dir, os.sep);
        return os.path.join(read_dir, f"{self.title}.mp3");

if __name__ == '__main__':
    url = "https://music.youtube.com/watch?v=8zK-gyVswxE&si=I-AR-dSskVzMvB_s"

    lmddownloader = LMDDownloader(url, "")
    title, down_path = lmddownloader.Download();

    lmdconvertor = LMDConvertor(title, down_path);
    lmdconvertor.Convert();

