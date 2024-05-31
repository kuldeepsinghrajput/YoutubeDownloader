from pytube import Playlist
import clipboard
import os
import re


p=Playlist(clipboard.paste()) 
dir= os.getcwd()+'\\STA\\'+re.sub("[^a-zA-Z]+", "",p.title)
print('download path= '+dir)
for video in p.videos:
	try:
		print('downloading : {} with url : {}'.format(video.title, video.watch_url))
		video.streams.filter(type='video', progressive=True, file_extension='mp4',res='720p').first().download(dir)
	except Exception as e:
		print(e)