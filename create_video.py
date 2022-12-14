import math
import cv2
import subprocess
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import audioread

FRAME_FILENAME = 'files/frame_image.png'
AUDIO_FILENAME = 'files/audio.wav'
VIDEO_FILENAME = 'files/video.avi'

def generate_frame(BG_IMAGE, title, image):
    if len(title) > 29:
        new_title = []
        last_id = 0
        for i in range(29, len(title), 29):
            idx = i
            while (title[idx] != " "):
                idx -= 1
            new_title.append(title[last_id:idx].center(29))
            last_id = idx + 1
        final_title = "\n".join(new_title)
    else:
        final_title = title

    img_w, img_h = image.size
    bg_w, bg_h = BG_IMAGE.size

    font = ImageFont.truetype('font/arial.ttf', 40)
    d = ImageDraw.Draw(BG_IMAGE)
    d.text((50, 100), final_title, fill=(0, 0, 0), font=font)
    BG_IMAGE.paste(image, ((bg_w-img_w)//2, (bg_h-img_h)//2))
    BG_IMAGE.save(FRAME_FILENAME)

def generate_audio(audio_text):
    audio_text = "..."+audio_text
    obj = gTTS(text=audio_text, lang='en')
    obj.save(AUDIO_FILENAME)
    with audioread.audio_open(AUDIO_FILENAME) as f:
        audio_length = math.ceil(f.duration)
    return audio_length

def generate_video(audio_length):
    out = cv2.VideoWriter(VIDEO_FILENAME, cv2.VideoWriter_fourcc(*'DIVX'), 1, (720, 1280))
    img = cv2.imread(FRAME_FILENAME)
    for i in range(audio_length+2):
        out.write(img)
    out.release()

def combine_audio_video(OUTPUT_FILENAME):
    cmd = f'ffmpeg -y -i {AUDIO_FILENAME} -r 30 -i {VIDEO_FILENAME} -filter:a aresample=async=1 -c:v copy {OUTPUT_FILENAME}'
    subprocess.call(cmd, shell=True)
    print("Video Generated Successfully!")

def create_video(news_title, news_summary, i):
    FRAME_SIZE = (720, 1280)
    BG_IMAGE = Image.new('RGB', FRAME_SIZE, color=(243, 250, 105))
    OUTPUT_FILENAME = f'files/output{i}.mkv'
    news_image = Image.open(f"files/news_img{i}.jpg")
    generate_frame(BG_IMAGE, news_title, news_image)
    audio_length = generate_audio(news_summary)
    generate_video(audio_length)
    combine_audio_video(OUTPUT_FILENAME)

