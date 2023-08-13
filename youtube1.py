from pytube import YouTube
link = "https://www.youtube.com/watch?v=mvZHDpCHphk"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
print("Download is completed successfully")