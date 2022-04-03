from pytube import YouTube
import os
print("\nDownload youtube videos as Mp3 \n")

URL = input("URL: ")
yt = YouTube(URL)

try:
  print("\nDownloading....\n")
  video = yt.streams.filter(only_audio=True).first()
  old = video.download()

  base, ext = os.path.splitext(old)
  new = base + ".mp3"
  os.rename(old, new)
  print("\n Downloaded Successfully\n")
except:
  print("\nTry Again, something went wrong\n")
