from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-80, 0), '99', font=myfont, fill=fillcolor)
    img.save('../image/result.jpg','jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('../image/0001.jpg')
    add_num(image)