from fileinput import filename

from asyncio import streams
from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import ffmpeg


# YouTube('https://youtu.be/Rc0smU6n-vM').streams.first().download()

# ��Ʃ�곪 ��Ʃ�� ���� �Ѵ� playlist�� ���� �� �ִ� �޼���
# pl = Playlist(
#     'https://music.youtube.com/playlist?list=OLAK5uy_nBl9St6mOl7S_8DxyvVOSVcIHm9-5nSHM&feature=shar')
# pl1 = pl[0]
# pl2 = pl[1]

url = "https://music.youtube.com/watch?v=SmJuzb-7p4E&si=EfehU-IG0_Qadils"
yt = YouTube(url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
# get_audio_only�� ����ϸ� �ڵ������� �ְ������� �޾��ش�.
# yt.streams.get_audio_only().download()

file_name = yt.streams.first().default_filename

# # file_name�� �����̸��� ����Ǵ� mp4���ϰ� �����ѵ�, ���α׷� �󿡼��� Ȯ���ڰ� 3gpp�ΰ��� ǥ�õǾ �ڿ������� �о .�� ã�Ƽ� .�� Ȯ���ڸ� ����� .mp4�� �����ϴ� �ڵ��̰�, save_name�� mp4�� mp3�� ��ȯ�ؼ� ������ ���� �̸��̴�.
file_name = file_name[0:file_name.rfind('.')]
save_name = file_name + ".mp3"
file_name += ".mp4";
print(save_name)


# ������ mp4���� mp3 320k ��ȯ�� �ȵǾ �Ʒ� ������ �����ϰ� �ٿ��� ���̽�, ��ȯ�� js�� �غ���.
# video = VideoFileClip(file_name)
# video.audio.write_audiofile('originfile.mp3')

# print(os.path.realpath('originfile.mp3'))
# print(os.getcwd())

# stream = ffmpeg.input(os.path.realpath('originfile.mp3'))
# stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, 'co.mp3')
# ffmpeg.run(stream)
