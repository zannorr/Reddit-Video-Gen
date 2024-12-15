import os, io
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import which
from moviepy import AudioFileClip

def text_to_speech(comments):
    if not os.path.exists('Audio'): os.makedirs('Audio')
    comment_path = 'Audio'
    for i, comment in enumerate(comments):
        tts = gTTS(text=comment, lang='en')
        tts.save(f'{comment_path}/comment_{i}.mp3')
        if i == 0: print(f'Successfully saved comment_{i}.mp3 (title)')
        else: print(f'Successfully saved comment_{i}.mp3')
    mp3_files = os.listdir(comment_path)
    return mp3_files, comment_path

def combine_mp3(mp3_files, comment_path):
    if not os.path.exists('AllAudio'): os.makedirs('AllAudio')
    final_output_path = os.path.join('AllAudio', 'combined_audio.mp3')
    mp3_path = os.path.join(comment_path , mp3_files[0])
    print(mp3_path)
    combined_mp3 = AudioSegment.from_mp3(mp3_path)
    for file in mp3_files[1:]:
        next_file_path = os.path.join(comment_path, file)
        next_file = AudioSegment.from_mp3(next_file_path)
        combined_mp3 += next_file
    combined_mp3.export(final_output_path, format = 'mp3')
    return final_output_path

def audio_length(audio_path):
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    return duration
