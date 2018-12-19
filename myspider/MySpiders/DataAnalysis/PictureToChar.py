#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将图片转化为字符图片
import sys
from PIL import Image, ImageFilter

# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("#.%$@?!~ ")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length                     # 为什么要加一呢？？？？？？？？
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    reload(sys)  # 为了下一行进行设置编码
    sys.setdefaultencoding('utf-8')
    im = Image.open(r'G:\image\IMG.jpg')
    im2 = im.filter(ImageFilter.DETAIL)
    im2.save("output.jpg")
    WIDTH,HEIGHT=im.size
    WIDTH/=4
    HEIGHT/=8
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
            # 这段代码是使用getpixel()方法获取某坐标像素点的RGBA值，再通过设置好的对应关系使图片被转换成字符画
            # PNG是一种使用RGBA的图像格式，其中A是指alpha即色彩空间
            # 然后使用get_char函数将这个值转换成字符，换行时加上换行符
            # 其中getpixel()方法会返回四个元素的元组，
            # 而get_char(im.getpixel((j, i )))使用了*则会把返回的元组元素依次赋给get_char()函数的四个参数
        txt +='\n'
    print txt
    with open("output.txt",'w') as f:
        f.write(txt)
