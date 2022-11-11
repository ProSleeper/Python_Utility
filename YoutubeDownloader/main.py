from asyncio import streams
from pytube import YouTube
from pytube import Playlist
# YouTube('https://youtu.be/Rc0smU6n-vM').streams.first().download()

# 유튜브나 유튜브 뮤직 둘다 playlist를 얻을 수 있는 메서드
pl = Playlist('https://music.youtube.com/playlist?list=OLAK5uy_nBl9St6mOl7S_8DxyvVOSVcIHm9-5nSHM&feature=shar');
pl1 = pl[0]
pl2 = pl[1]


yt = YouTube('https://www.youtube.com/watch?v=-H85_VMl3iI&ab_channel=LikeItMusic')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
yt.streams.get_audio_only().download()  # get_audio_only를 사용하면 자동적으로 최고음질로 받아준다.

# yt.streams.filter(bitrate="320kbps", progressive=False).first().download(filename="audio.mp3")
