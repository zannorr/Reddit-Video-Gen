from createVideo import clip_video, combine_video_audio_picture, crop_to_vertical
from fetchComments import fetch_comment_text
from fetchAudio import text_to_speech, combine_mp3, audio_length
from fetchVideo import download_youtube_video
from titleImage import capture_title_image
from cleanup import delete_specific_folders_in_current_directory
from subtitleGen import transcription

def start_menu():
    while True:
        print(
            f"{'-'*50}\nShort-Video Creation Tool v1.1.0\n(Last Update 12/14/2024)\nAuthor: Zander Norris\n{'-'*50}"
        )
        print(f"Options:\n1. Create Short Video\n2. Settings\n3. Exit\n{'-'*50}")
        try:
            flag = int(input("Please enter 1-3: "))
            if flag in [1,2,3]:
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
    reddit_url = input("What is the link of the reddit thread? ")
    youtube_url = input("What is the link for the youtube video? ")

    title_path = capture_title_image(reddit_url)
    comments = fetch_comment_text(reddit_url)

    mp3_files, comment_audio_path = text_to_speech(comments)

    combined_audio = combine_mp3(mp3_files, comment_audio_path)

    video_path = download_youtube_video(youtube_url)
    start_time = 45
    end_time = audio_length(combined_audio) + start_time

    clipped_video_path = clip_video(video_path, start_time, end_time)

    cropped_video_path = crop_to_vertical(clipped_video_path)

    output_path = combine_video_audio_picture(
        cropped_video_path, combined_audio, title_path
    )
    # create subtitles
    transcription(output_path)
    print('Successfully created video.')


def settings():
    while True:
        print(f"{'-'*50}\nUser settings:\n1. Client ID\n2. Client Secret\n3. User Agent\n4. Clear Cache\n5. Exit to main menu\n{'-'*50}")
        try:
            flag = int(input("Please enter 1-5: "))
            if flag in [1,2,3,4,5]:
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
        temp_dir = ["titleImage", "VideoFiles", "Audio", "AllAudio", "ClippedVideo"]
        delete_specific_folders_in_current_directory(temp_dir)
    elif flag == 5:
        start_menu()


if __name__ == "__main__":
    start_menu()
    # while True:
    #     print(
    #         f"{'-'*50}\nShort-Video Creation Tool v1.1.0\n(Last Update 12/14/2024)\nAuthor: Zander Norris\n{'-'*50}"
    #     )
    #     print("Options:\n1. Create Short Video\n2. Settings")
    #     try:
    #         flag = int(input("Please enter 1-2: "))
    #         if flag == 1 or flag == 2:
    #             break
    #         else:
    #             print("Invalid Input. Please enter 1-2.")
    #     except ValueError:
    #         print("Invalid Input. Please enter an integer.")
    # if flag == 1:
    #     reddit_url = input("What is the link of the reddit thread? ")
    #     youtube_url = input("What is the link for the youtube video? ")

    #     title_path = capture_title_image(reddit_url)
    #     comments = fetch_comment_text(reddit_url)

    #     mp3_files, comment_audio_path = text_to_speech(comments)

    #     combined_audio = combine_mp3(mp3_files, comment_audio_path)

    #     video_path = download_youtube_video(youtube_url)
    #     start_time = 45
    #     end_time = audio_length(combined_audio) + start_time

    #     clipped_video_path = clip_video(video_path, start_time, end_time)

    #     cropped_video_path = crop_to_vertical(clipped_video_path)

    #     output_path = combine_video_audio_picture(
    #         cropped_video_path, combined_audio, title_path
    #     )
    #     # create subtitles
    #     transcription(output_path)
    #     # delete_specific_folders_in_current_directory(temp_dir)
    # elif flag == 2:
    # while True:
    #     print("User settings:\n1. Client ID\n2. Client Secret\n3. User Agent")
    #     try:
    #         flag = int(input("Please enter 1-3: "))
    #         if flag == 1 or flag == 2 or flag == 3:
    #             break
    #         else:
    #             print("Invalid Input. Please enter 1-2.")
    #     except ValueError:
    #         print("Invalid Input. Please enter an integer.")
    # if flag == 1:
    #     client_id = input("Please enter client ID: ")
    #     with open("clientid.txt", "w") as file:
    #         file.write(client_id)
    #         print("Successfully wrote client ID to memory.")
    # elif flag == 2:
    #     client_secret = input("Please enter client secret: ")
    #     with open("clientsecret.txt", "w") as file:
    #         file.write(client_secret)
    #         print("Successfuly wrote client secret to memory.")
    # elif flag == 3:
    #     user_agent = input("Please enter user agent: ")
    #     with open("useragent.txt", "w") as file:
    #         file.write(user_agent)
    #         print("Successfully wrote user agent to memory.")
