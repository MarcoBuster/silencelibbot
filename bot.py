from PIL import Image, ImageDraw, ImageFont
image = Image.open('preset/crab.jpg')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('font/Roboto-Regular.ttf', size=63)
(x, y) = (15, 81)
message = "the quick brown fox jumps over the lazy dog"
color = 'rgb(255, 255, 255)'
draw.text((x, y), message, fill=color, font=font)
image.save('test/test.jpg')
