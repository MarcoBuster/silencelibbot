import os
import random
import config

import botogram
from PIL import Image, ImageDraw, ImageFont

bot = botogram.create(config.BOT_TOKEN)

def _convert_image(text):
    image = Image.open('template/crab.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('font/Roboto-Regular.ttf', size=63)
    (x, y) = (15, 81)
    message = text
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), message, fill=color, font=font)
    output_path = 'output/out_{n}.jpg'.format(n=random.randint(0, 1000000))
    image.save(output_path)
    return output_path

@bot.process_message
def process_messages(chat, message):
    if not message.text:
        return

    output_path = _convert_image(message.text)
    message.reply_with_photo(path=output_path)
    os.remove(output_path)

if __name__ == '__main__':
    bot.run()
