from createVideo import clip_video, combine_video_audio_picture, crop_to_vertical
from fetchComments import fetch_comment_text
from fetchAudio import text_to_speech, combine_mp3, audio_length
from fetchVideo import download_youtube_video
from titleImage import capture_title_image
from cleanup import delete_specific_folders_in_current_directory
from subtitleGen import transcription

temp_dir = ['titleImage', 'VideoFiles', 'AudioFiles', 'AggregatedAudio', 'ClippedVideo']
if __name__ == '__main__':
    print('Welcome to generative short video creation!')
    print('-'*50)
    
    # reddit_url = input('What is the link of the reddit thread? ')
    # youtube_url = input('What is the link for the youtube video? ')

    reddit_url = 'https://www.reddit.com/r/AskReddit/comments/1hdueny/what_are_the_signs_youve_noticed_that_youre/'
    youtube_url = 'https://www.youtube.com/watch?v=u7kdVe8q5zs&t=13s'

    title_path = capture_title_image(reddit_url)
    comments = fetch_comment_text(reddit_url)

    mp3_files, comment_audio_path = text_to_speech(comments)

    combined_audio = combine_mp3(mp3_files, comment_audio_path)

    video_path = download_youtube_video(youtube_url)
    start_time = 45
    end_time = audio_length(combined_audio) + start_time

    clipped_video_path = clip_video(video_path, start_time, end_time)

    cropped_video_path = crop_to_vertical(clipped_video_path)

    output_path = combine_video_audio_picture(cropped_video_path, combined_audio, title_path)
    # create subtitles
    transcription(output_path)
    # delete_specific_folders_in_current_directory(temp_dir)

