from moviepy.editor import *
from fetchAudio import audio_length
import os
title_comment = 'AudioFiles\comment_0.mp3'

def clip_video(video_path, start_time, end_time):
    if not os.path.exists('ClippedVideo'):
        os.makedirs('ClippedVideo')
    output_path = os.path.join('ClippedVideo', 'clippedVideo.mp4')
    with VideoFileClip(video_path) as video:
        clipped = video.subclip(start_time, end_time)
        clipped.write_videofile(output_path, codec='libx264', bitrate = '5000k')
    return output_path

import os
from moviepy.editor import VideoFileClip

def crop_to_vertical(input_file, target_width=1080, target_height=1920):
    if not os.path.exists('FinalVideo'):
        os.makedirs('FinalVideo')
    
    output_file = os.path.join('FinalVideo', 'croppedFinalVideo.mp4')
    
    # Load the video
    clip = VideoFileClip(input_file)
    
    # Calculate the cropping dimensions
    video_width, video_height = clip.size
    aspect_ratio = video_height / video_width
    new_width = target_width
    new_height = int(target_width * aspect_ratio)
    
    # Ensure the new height matches the target aspect ratio (9:16)
    if new_height < target_height:
        new_height = target_height
        new_width = int(target_height / aspect_ratio)
    
    # Center the crop if the new width is larger than the target width
    x_center = (new_width - target_width) / 2 if new_width > target_width else 0
    y_center = (new_height - target_height) / 2 if new_height > target_height else 0
    
    # Resize and crop the video
    clip = clip.resize((new_width, new_height))
    clip = clip.crop(x_center, y_center, width=target_width, height=target_height)
    
    # Write the cropped video to the output file with higher bitrate
    clip.write_videofile(output_file, codec="libx264", fps=24, bitrate="5000k")
    
    return output_file

def combine_video_audio_picture(video_path, audio_path, title_path):
    output_path = os.path.join('FinalVideo', 'finalVideo.mp4')
    title_clip = ImageClip(title_path).resize(2).set_duration(audio_length(title_comment))
    audio_clip = AudioFileClip(audio_path)
    video_clip = VideoFileClip(video_path)
    
    composite_clip = CompositeVideoClip([video_clip.set_audio(audio_clip), title_clip.set_position(("center", "center"))])

    composite_clip.write_videofile(output_path, codec='libx264', fps=24, bitrate = '5000k')

    # if os.path.exists('FinalVideo\\croppedFinalVideo.mp4'):
    #     os.remove('FinalVideo\\croppedFinalVideo.mp4')
    return output_path

