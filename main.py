from createVideo import (
    clip_video,
    combine_video_audio_picture,
    crop_to_vertical,
    combine_video_audio_multiple_pictures,
)
from fetchComments import fetch_comment_text
from fetchAudio import text_to_speech, combine_mp3, audio_length, video_length, create_text_image
from fetchVideo import download_youtube_video
from imageCapture import capture_text
from cleanup import delete_specific_folders_in_current_directory
from subtitleGen import transcription
import random as r


def start_menu():
    while True:
        print(
            f"{'-'*50}\nShort-Video Creation Tool v1.1.0\n(Last Update 12/14/2024)\nAuthor: Zander Norris\n{'-'*50}"
        )
        print(f"Options:\n1. Create Short Video\n2. Settings\n3. Exit\n{'-'*50}")
        try:
            flag = int(input("Please enter 1-3: "))
            if flag in [1, 2, 3]:
                break
            else:
                print("Invalid Input. Please enter 1-3.")
        except ValueError:
            print("Invalid Input. Please enter an integer.")
    if flag == 1:
        create_short_video()
    elif flag == 2:
        settings()
    elif flag == 3:
        exit()


def create_short_video():
    reddit_url = input("URL of Reddit thread: ")
    youtube_url = input("URL of YouTube thread: ")
    while True:
        try:
            num_comments = min(int(input("Number of comments (max 15): ")), 15)
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")
    title_path = capture_text(reddit_url)
    comments = fetch_comment_text(reddit_url, num_comments)

    tts_comments = text_to_speech(comments)

    combined_audio = combine_mp3(tts_comments)

    video_path = download_youtube_video(youtube_url)
    flag = input("Specific start time of video (Y/N): ").upper()
    while flag not in ["Y", "N"]:
        flag = input("Specific start time of video (Y/N): ").upper()
    if flag == "Y":
        while True:
            try:
                start_time = int(input("Start time of video (In Seconds):"))
                break
            except ValueError:
                print("Invalid Input. Please enter an integer.")
    elif flag == "N":
        start_time = r.randint(
            0,
            (int(video_length(video_path)) - int((audio_length(combined_audio) - 10))),
        )
    end_time = audio_length(combined_audio) + start_time

    clipped_video_path = clip_video(video_path, start_time, end_time)

    cropped_video_path = crop_to_vertical(clipped_video_path)
    while True:
        try:
            print("Options:\n1.Subtitles\n2. None")
            flag = int(input("Select 1-3: "))
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")
    if flag == 1:
        output_path = combine_video_audio_picture(
            cropped_video_path, combined_audio, title_path
        )
        transcription(output_path)
    elif flag == 2:
        print(f"Successfully created video. Location : {output_path}.")


def settings():
    while True:
        print(
            f"{'-'*50}\nUser settings:\n1. Client ID\n2. Client Secret\n3. User Agent\n4. Clear Cache\n5. Exit to main menu\n{'-'*50}"
        )
        try:
            flag = int(input("Please enter 1-5: "))
            if flag in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid Input. Please enter 1-2.")
        except ValueError:
            print("Invalid Input. Please enter an integer.")
    if flag == 1:
        client_id = input("Please enter client ID: ")
        with open("clientid.txt", "w") as file:
            file.write(client_id)
            print("Successfully wrote client ID to memory.")
            settings()
    elif flag == 2:
        client_secret = input("Please enter client secret: ")
        with open("clientsecret.txt", "w") as file:
            file.write(client_secret)
            print("Successfuly wrote client secret to memory.")
            settings()
    elif flag == 3:
        user_agent = input("Please enter user agent: ")
        with open("useragent.txt", "w") as file:
            file.write(user_agent)
            print("Successfully wrote user agent to memory.")
            settings()
    elif flag == 4:
        temp_dir = ["Images", "VideoFiles", "Audio", "AllAudio", "ClippedVideo", 'textImages']
        delete_specific_folders_in_current_directory(temp_dir)
    elif flag == 5:
        start_menu()


if __name__ == "__main__":
    start_menu()
