import whisper
from moviepy.editor import VideoFileClip
import ffmpeg
import os
# Load the Whisper model
def transcription(video_path):
    model = whisper.load_model("base")

    # Load the video file
    video = VideoFileClip(video_path)

    # Extract audio from video
    audio_path = os.path.join('AggregatedAudio', 'temp_audio.wav')
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')

    # Transcribe audio
    result = model.transcribe(audio_path)

    # Create SRT file
    srt_path = "subtitles.srt"
    with open(srt_path, "w") as srt_file:
        for i, segment in enumerate(result["segments"]):
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"]

            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time % 1) * 1000):03} --> {int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time % 1) * 1000):03}\n")
            srt_file.write(f"{text}\n\n")

    input('Check subtitles in srt file, then press enter to continue...')

    # Path to the output video
    output_video_path = os.path.join('FinalVideo', 'output_video_with_subtitles.mp4')
    vf_filter = f"subtitles={srt_path}:force_style='MarginV=30'"
    # Add subtitles to the video
    ffmpeg.input(video_path).output(output_video_path, vf=vf_filter, acodec = 'copy').run()

#testing purposes
if __name__ == '__main__':
    transcription('FinalVideo\\finalVideo.mp4')
    
