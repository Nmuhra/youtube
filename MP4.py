from pytube import YouTube

link = input("Video URL:\n")
url = str(link)
my_video = YouTube(url)

print("Video Title: ")
print(my_video.title)

print("Tumbnail Image url: ")
print(my_video.thumbnail_url)

print("Download the video: ") 
for stream in my_video.streams:
    print(stream)
  
my_video = my_video.streams.get_highest_resolution()
my_video.download()
