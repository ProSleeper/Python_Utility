from fileinput import filename

from asyncio import streams
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import os
import ffmpeg


# YouTube('https://youtu.be/Rc0smU6n-vM').streams.first().download()

# 유튜브나 유튜브 뮤직 둘다 playlist를 얻을 수 있는 메서드
# pl = Playlist('https://music.youtube.com/playlist?list=OLAK5uy_nBl9St6mOl7S_8DxyvVOSVcIHm9-5nSHM&feature=shar');
# pl1 = pl[0]
# pl2 = pl[1]


# yt = YouTube('https://music.youtube.com/watch?v=6U2h_iccLXE&feature=share')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
# # yt.streams.get_audio_only().download()  # get_audio_only를 사용하면 자동적으로 최고음질로 받아준다.

# file_name = yt.streams.first().default_filename

# # file_name은 파일이름은 저장되는 mp4파일과 동일한데, 프로그램 상에서는 확장자가 3gpp인가로 표시되어서 뒤에서부터 읽어서 .을 찾아서 .과 확장자를 지우고 .mp4로 저장하는 코드이고, save_name은 mp4를 mp3로 변환해서 저장할 파일 이름이다.
# file_name = file_name[0:file_name.rfind('.')]
# save_name = file_name + ".mp3"
# file_name += ".mp4";
# print(save_name)

# video = VideoFileClip(file_name)
# video.audio.write_audiofile('originfile.mp3')

print(os.path.realpath('originfile.mp3'))
print(os.getcwd())

stream = ffmpeg.input(os.path.realpath('originfile.mp3'))
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'co.mp3')
ffmpeg.run(stream)
