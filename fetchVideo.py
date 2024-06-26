from pytube import YouTube
import os

def download_youtube_video(url, output_dir='VideoFiles'):
    # Create directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        yt = YouTube(url)
    except Exception as e:
        print('Connection Error:', e)
        return None

    # Filter streams and select the highest resolution mp4 stream
    mp4_streams = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
    if not mp4_streams:
        print("No mp4 streams available.")
        return None

    dl_video = mp4_streams.first()

    # Define the complete output path including the filename
    output_path = os.path.join(output_dir, 'full_video.mp4')
    try:
        dl_video.download(output_path=output_dir, filename='full_video.mp4')
        print('Download successful.')
    except Exception as e:
        print("Error downloading video:", e)
        return None

    return output_path
