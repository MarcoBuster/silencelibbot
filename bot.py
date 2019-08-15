import botogram
import config
from PIL import Image, ImageDraw, ImageFont

bot = botogram.create(config.BOT_TOKEN)

@bot.process_message
def process_messages(chat, message):
    if not message.photo:
        return

    output/output.jpg = image = Image.open('template/crab.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('font/Roboto-Regular.ttf', size=63)
    (x, y) = (15, 81)
    message = "message"
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), message, fill=color, font=font)
    image.save('output/output.jpg')(message.photo)

    message.reply_with_photo(path=output/output.jpg)

if __name__ == '__main__':
    bot.run()
