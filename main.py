from createVideo import clip_video, combine_video_audio_picture, crop_to_vertical
from fetchComments import fetch_comment_text
from fetchAudio import text_to_speech, combine_audio_files, audio_length
from fetchVideo import download_youtube_video
from titleImage import capture_title_image
from cleanup import delete_specific_folders_in_current_directory

temp_dir = ['titleImage', 'VideoFiles', 'AudioFiles', 'AggregatedAudio', 'ClippedVideo']
if __name__ == '__main__':
    print('Welcome to Reddit video creation')

    reddit_url = input('What is the link of the reddit thread? ')
    youtube_url = input('What is the link for the youtube video? ')

    title_path = capture_title_image(reddit_url)
    comments = fetch_comment_text(reddit_url)

    comments_audio = text_to_speech(comments)
    aggregated_comments_audio = combine_audio_files(comments_audio)

    video_path = download_youtube_video(youtube_url)
    start_time = 45
    end_time = audio_length(aggregated_comments_audio) + start_time

    clipped_video_path = clip_video(video_path, start_time, end_time)

    cropped_video_path = crop_to_vertical(clipped_video_path)

    combine_video_audio_picture(cropped_video_path, aggregated_comments_audio, title_path)

    delete_specific_folders_in_current_directory(temp_dir)

