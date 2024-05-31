from pytube import YouTube
import clipboard
import os
import re
try:
	YouTube(clipboard.paste()).streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution().download(os.getcwd()+'\\STA\\')
except Exception as e:
	print(e)

