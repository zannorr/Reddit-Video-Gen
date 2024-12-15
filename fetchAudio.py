import os, io
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import which
from moviepy import AudioFileClip, VideoFileClip
from PIL import Image, ImageDraw, ImageFont
import whisper
import textwrap
def text_to_speech(comments):
    if not os.path.exists('Audio'): os.makedirs('Audio')
    comment_path = 'Audio'
    for i, comment in enumerate(comments):
        tts = gTTS(text=comment, lang='en')
        tts.save(f'{comment_path}/comment_{i}.mp3')
        if i == 0: print(f'Successfully saved comment_{i}.mp3 (title)')
        else: print(f'Successfully saved comment_{i}.mp3')
    mp3_files = os.listdir(comment_path)
    return mp3_files

def combine_mp3(mp3_files, comment_path = 'Audio'):
    if not os.path.exists('AllAudio'): os.makedirs('AllAudio')
    final_output_path = os.path.join('AllAudio', 'combined_audio.mp3')
    mp3_path = os.path.join(comment_path , mp3_files[0])
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

def video_length(video_path):
    video_clip = VideoFileClip(video_path)
    duration = video_clip.duration
    return duration

# def create_text_image(mp3_path='Audio', image_width=200, image_height=200, font_size=14):
#     # Load the model once outside the loop for efficiency
#     model = whisper.load_model("base")
    
#     # Create output directories if they don't exist
#     os.makedirs('textImages', exist_ok=True)
#     os.makedirs('Images', exist_ok=True)
    
#     output_files = []
    
#     # Get sorted list of MP3 files to ensure consistent processing
#     mp3_files = sorted([f for f in os.listdir(mp3_path) if f.endswith('.mp3')])
    
#     for i, filename in enumerate(mp3_files):
#         # Skip first file if needed
#         if i == 0:
#             continue
        
#         # Full path to the MP3 file
#         mp3_file_path = os.path.join(mp3_path, filename)
        
#         try:
#             # Transcribe audio
#             result = model.transcribe(mp3_file_path)
#             transcribed_text = result["text"]
            
#             # Create image with white background
#             img = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
#             draw = ImageDraw.Draw(img)
            
#             # Use a more readable font
#             try:
#                 font = ImageFont.truetype("arial.ttf", font_size)
#             except IOError:
#                 font = ImageFont.load_default()
            
#             # Wrap text to fit image width
#             wrapped_text = textwrap.fill(transcribed_text, width=30)
            
#             # Draw text with better positioning
#             draw.text((10, 10), wrapped_text, font=font, fill=(0, 0, 0))
            
#             # Save image
#             output_path = os.path.join('Images', f'comment_{i}.png')
#             img.save(output_path)
            
#             print(f'Successfully saved transcription to {output_path}')
#             output_files.append(output_path)
        
#         except Exception as e:
#             print(f"Error processing {filename}: {e}")
    
#     return output_files

if __name__ == '__main__':
    create_text_image()
