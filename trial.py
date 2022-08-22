from PIL import Image
img = Image.open('car.jpg', 'r')
img_w, img_h = img.size
# background = Image.new('RGBA', (720, 1280), (239, 245, 56, 255))
background = Image.open('frame_image.png')
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, (-500, 500))
background.save('out.png')
