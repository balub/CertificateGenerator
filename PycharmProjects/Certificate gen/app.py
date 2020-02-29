from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

text = "Balu B Naidu"

img = Image.open('certificate.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 80)
draw.text((300, 375), text, (46, 55, 65), font=font)
img.save('position.png')
 