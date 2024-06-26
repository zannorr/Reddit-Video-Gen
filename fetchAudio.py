from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.utils import which
from moviepy.editor import AudioFileClip

AudioSegment.converter = which("ffmpeg")

def text_to_speech(comments):
    if not os.path.exists('AudioFiles'):
        os.makedirs('AudioFiles')

    audio_files = []
    for i, comment in enumerate(comments):
        tts = gTTS(text=comment, lang='en')
        file_path = os.path.join('AudioFiles', f'comment_{i}.mp3')
        tts.save(file_path)
        audio_files.append(file_path)
        print(f'Successfully saved comment_{i}.mp3...')
    return audio_files

def combine_audio_files(audio_files):
    if not os.path.exists('AggregatedAudio'):
        os.makedirs('AggregatedAudio')
    output_path = os.path.join('AggregatedAudio', 'combined_audio.mp3')
    combined = AudioSegment.empty()
    for file_path in audio_files:
        audio = AudioSegment.from_mp3(file_path)
        combined += audio
    combined.export(output_path, format='mp3')
    print('Successfully combined audio files...')
    return output_path

def audio_length(audio_path):
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    return duration
