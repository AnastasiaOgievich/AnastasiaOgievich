from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

start_day = datetime(2022, 3, 1)  

today = datetime.now()
days_streak = (today - start_day).days

image = Image.new('RGB', (200, 60), color=(73, 109, 137))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", 40)

draw.text((10, 10), f"{days_streak} days", font=font, fill=(255, 255, 255))

image.save('duolingo_streak.png')
