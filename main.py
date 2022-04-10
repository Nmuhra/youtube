from pytube import YouTube
import os
URL = input("URL: ")
choice = input("MP3 or MP4:\n").lower()
yt = YouTube(URL)
if choice == "mp3":
  try:
    print("Downloading...")
    video = yt.streams.filter(only_audio=True).first()
    old = video.download()

    base, ext = os.path.splitext(old)
    new = base + ".mp3"
    os.rename(old, new)
    print("\n Downloaded Successfully\n")
  except:
    print("\nTry Again, something went wrong\n")

if choice == "mp4":
  print("Video Title: ")
  print(yt.title)

  print("Tumbnail Image url: ")
  print(yt.thumbnail_url)

  print("Download the video: ") 
  for stream in yt.streams:
    print(stream)
  
  my_video = yt.streams.get_highest_resolution()
  my_video.download()
