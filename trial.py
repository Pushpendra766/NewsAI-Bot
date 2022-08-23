import math

from gtts import gTTS
from mutagen.wave import WAVE
import audioread

text = "The most iconic donut shop in Hollywood is Randy's Donuts. It has appeared in many movies including Crocodile Dundee and Iron Man 2."
lang = 'hi'
obj = gTTS(text=text, lang=lang)
obj.save("sample.wav")
with audioread.audio_open('sample.wav') as f:
    print(math.ceil(f.duration))
# audio = WAVE("sample.wav")
# print(audio.info.length)