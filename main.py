import json
import random
from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
from breaklines import break_into_lines


def video_maker(image, text, audio):
    audio_clip = AudioFileClip(audio)
    background_image_clip = ImageClip(image, duration=audio_clip.duration)
    text_to_add = break_into_lines(text, 40)
    text_clip = TextClip(text_to_add, fontsize=30, color='white', font='Helvetica-Bold')    
    text_clip = text_clip.set_duration(background_image_clip.duration)
    text_clip = text_clip.set_position(('center', 'center'))

    final_clip = CompositeVideoClip([background_image_clip, text_clip.set_audio(audio_clip)])

    final_clip.write_videofile("export.mp4", codec='libx264', audio_codec='aac', fps=1)


#load text
f = open("./assets/quotes/stoic.json")
data = json.load(f)
text = (data['quotes'][random.randint(0,(len(data['quotes'])))]['quote'])

#load audio
audio = "./assets/audio/audio-1.mp3"

#load image
image = "./assets/images/image-1.jpg"

video_maker(image, text, audio)


