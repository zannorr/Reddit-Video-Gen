from pytube import YouTube
import os
def download_youtube_video(url):
    if not os.path.exists('VideoFiles'):
        os.makedirs('VideoFiles') 
    video_path = 'VideoFiles/full_video.mp4'
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    download = stream.download(filename=video_path)
    return video_path
