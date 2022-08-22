import cv2
import subprocess
import pyttsx3
from mutagen.wave import WAVE
from PIL import Image, ImageDraw, ImageFont

def generate_frame(BG_IMAGE, title, image):
    if len(title) > 27:
        # below line will add \n after every 27 character, so that whole title be visible
        final_title = "\n".join(title[i:i+27] for i in range(0, len(title), 27))
    else:
        final_title = title

    img_w, img_h = image.size
    bg_w, bg_h = BG_IMAGE.size

    font = ImageFont.truetype('arial.ttf', 40)
    d = ImageDraw.Draw(BG_IMAGE)
    d.text((50, 100), final_title, fill=(0, 0, 0), font=font)
    BG_IMAGE.paste(image, ((bg_w-img_w)//2, (bg_h-img_h)//2))
    BG_IMAGE.save(FRAME_FILENAME)

def generate_audio(audio_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(audio_text, AUDIO_FILENAME)
    engine.runAndWait()
    audio = WAVE(AUDIO_FILENAME)
    return int(audio.info.length)

def generate_video(audio_length):
    out = cv2.VideoWriter(VIDEO_FILENAME, cv2.VideoWriter_fourcc(*'DIVX'), 1, (720, 1280))
    img = cv2.imread(FRAME_FILENAME)
    for i in range(audio_length+2):
        out.write(img)
    out.release()

def combine_audio_video():
    cmd = f'ffmpeg -y -i {AUDIO_FILENAME} -r 30 -i {VIDEO_FILENAME} -filter:a aresample=async=1 -c:v copy {OUTPUT_FILENAME}'
    subprocess.call(cmd, shell=True)
    print("Video Generated Successfully!")

if __name__ == "__main__":
    FRAME_SIZE = (720, 1280)
    BG_IMAGE = Image.new('RGB', FRAME_SIZE, color=(243, 250, 105))
    FRAME_FILENAME = 'files/frame_image.png'
    AUDIO_FILENAME = 'files/audio.wav'
    VIDEO_FILENAME = 'files/video.avi'
    OUTPUT_FILENAME = 'files/output.mkv'

    news_title = "a1a2aawsesr3a4a 5a6a7a8a9a1a2b1b2b3b4b5b6"
    news_image = Image.open("car.jpg")
    news_summary = "Manchester United's hopes of unveiling casemiro have been dealt a blow over a problem with the midfielder's visa, according to reports. The transfer was 'subject to the agreement of personal terms, UK visa requirements and a medical' the 30-year-old has encountered some issues with his visa, so the deal will not be rubberstamped for several more days."
    generate_frame(BG_IMAGE, news_title, news_image)
    audio_length = generate_audio(news_summary)
    generate_video(audio_length)
    combine_audio_video()

