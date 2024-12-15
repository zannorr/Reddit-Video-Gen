from moviepy import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
from fetchAudio import audio_length
from imageCapture import capture_text
import os

def clip_video(video_path, start_time, end_time):
    if not os.path.exists('ClippedVideo'):
        os.makedirs('ClippedVideo')
    output_path = os.path.join('ClippedVideo', 'clippedVideo.mp4')
    clip = VideoFileClip(video_path)
    clip = clip.subclipped(start_time, end_time)
    clip.write_videofile(output_path)
    return output_path


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
    clip = clip.resized((new_width, new_height))
    clip = clip.cropped(x_center, y_center, width=target_width, height=target_height)
    
    # Write the cropped video to the output file with higher bitrate
    clip.write_videofile(output_file, codec="libx264", fps=24, bitrate="5000k")
    
    return output_file

def combine_video_audio_picture(video_path, audio_path, title_path):
    title_comment = 'Audio\comment_0.mp3'
    output_path = os.path.join('FinalVideo', 'finalVideo.mp4')
    title_clip = ImageClip(title_path).resized(1.25).with_duration(audio_length(title_comment))
    audio_clip = AudioFileClip(audio_path)
    video_clip = VideoFileClip(video_path)
    
    composite_clip = CompositeVideoClip([video_clip.with_audio(audio_clip), title_clip.with_position(("center", "center"))])

    composite_clip.write_videofile(output_path, codec='libx264', fps=24, bitrate = '5000k')

    # if os.path.exists('FinalVideo\\croppedFinalVideo.mp4'):
    #     os.remove('FinalVideo\\croppedFinalVideo.mp4')
    return output_path

# def combine_video_audio_multiple_pictures(video_path, audio_path, title_path, comment_list):
#     title_comment = 'Audio\comment_0.mp3'
#     output_path = os.path.join('FinalVideo', 'finalVideo.mp4')
#     title_clip = ImageClip(title_path).resized(1.25).with_duration(audio_length(title_comment))
#     comment_clips = []
#     for i, comment_path in enumerate(comment_list):
#         clip = (
#             ImageClip(comment_path)
#             .resized(1.5)
#             .with_duration(audio_length(comment_path))
#         )
#         comment_clips.append(clip)

#     # Combine all image clips (title + comments) sequentially
#     image_video = concatenate_videoclips([title_clip] + comment_clips, method="compose")

#     # Load the base video
#     base_video = VideoFileClip(video_path)
#     audio_clip = AudioFileClip(audio_path)
#     # Overlay the image sequence on top of the base video
#     final_video = CompositeVideoClip([base_video.with_audio(audio_clip), image_video.with_position("center")])

#     # Write the output video
#     final_video.write_videofile(output_path, codec='libx264', fps=24, bitrate = '5000k')

#     return output_path

if __name__ == '__main__':
    comment_list = capture_text(reddit_url='https://www.reddit.com/r/AskReddit/comments/1he32qp/whats_the_stupidest_question_youve_ever_been_asked/')
    combine_video_audio_multiple_pictures(video_path='FinalVideo\\croppedFinalVideo.mp4', audio_path='AllAudio\\combined_audio.mp3', title_path='Images\\title_screenshot.png', comment_list=comment_list)