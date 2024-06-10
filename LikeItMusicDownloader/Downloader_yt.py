#-*- coding: euc-kr -*-

import yt_dlp

# URLS = ['https://music.youtube.com/watch?v=3d-QZBwMMq8&si=mcQSQvQkRtzgaopu']

# ydl_opts = {
#     'format': 'bestaudio/best',
#     # ?? See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
#     # 'outtmpl':'../call'
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)


class LMDDownloader:
    def __init__(self, url:str, save_dir:str):
        try:
            self.url = url
            self.save_dir = save_dir
            # self.trim_title = self.__Trim_Title()
            self.ydl_opts = {
                'format': 'best',
                # ?? See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
                # 'postprocessors': [{  # Extract audio using ffmpeg
                #     'key': 'FFmpegExtractAudio',
                #     'preferredcodec': 'mp3',
                #     'preferredquality': '320',
                   
                # }],
                # 'outtmpl':self.save_dir
            }   
            
        except BaseException as e:
            print(f"[{self.__class__.__name__}], Error: {str(e)}")
        
        
    def Download(self):
        # download가 완료 되면 다운로드한 file path를 리턴해준다.
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            error_code = ydl.download(self.url)
    
        
    # def __Trim_Title(self):
    #     return f"{self.yt.title.replace(' ', '')}.mp4"