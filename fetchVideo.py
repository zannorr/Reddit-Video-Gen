import yt_dlp
import os
def download_youtube_video(youtube_url, output_path='VideoFiles', custom_title='full_video'):
    try:
        ydl_opts = {
            'format': 'best',  # Download best quality
        }
        
        if output_path:
            if custom_title:
                ydl_opts['outtmpl'] = f'{output_path}/{custom_title}.%(ext)s'
            else:
                ydl_opts['outtmpl'] = f'{output_path}/%(title)s.%(ext)s'
        elif custom_title:
            ydl_opts['outtmpl'] = f'{custom_title}.%(ext)s'
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            
        print("Download completed!")
        
    except Exception as e:
        print("An error occurred:", str(e))

    return os.path.join(output_path, f'{custom_title}.mp4')