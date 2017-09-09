from PIL import Image, ImageFont, ImageDraw
img = Image.open('prof.jpg').convert('RGB')
w, h = img.size
pixels = img.load()
fontsize = 15
fontpath = '/System/Library/Fonts/Menlo.ttc'
# On windows, fontpath = 'C://Windows/Fonts/msgothic.ttc'
# On Mac, fontpath ='/System/Library/Fonts/Menlo.ttc'
font = ImageFont.truetype(fontpath, fontsize, encoding='utf-8')
output_img = Image.new(mode='RGBA', size=(w,h), color=(255,255,255))
draw = ImageDraw.Draw(output_img)
for y in range(0, h, fontsize): # The third parameter in range is a step 
    for x in range(0, w, fontsize):
        r, g, b = pixels[x, y]
        gray = r * 0.2326 + g * 0.7152 + b * 0.0722
        if gray  > 225:
            character = '.'
        elif gray > 200:
            character = ':'
        elif gray > 175:
            character = '¥'
        elif gray > 150:
            character = '$'
        elif gray > 125:
            character = ';'
        elif gray > 100:
            character = '+'
        elif gray > 75:
            character = '*'
        elif gray > 50:
            character = '%'
        elif gray > 25:
            character = '#'
        else:
            character = 'W'
        draw.text((x, y), character, font=font, fill = '#000000') # #000000 corresponds black
output_img.show()