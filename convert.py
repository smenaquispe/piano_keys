from moviepy import *
from moviepy.editor import *

audio = AudioFileClip("audio.mp3")  

audio.write_audiofile("audio2.mp3")
