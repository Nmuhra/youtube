from pytube import YouTube

url = str(input("url: "))
video = YouTube(url)

print("Video Title: ")
print(video.title)

print("Tumbnail Image:\n")
print(video.thumbnail_url)

print("Download video")
print("Downloading...")
video = video.streams.get_highest_resolution()
video.download()


