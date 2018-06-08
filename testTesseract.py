# -*- coding=utf-8 -*-
from PIL import Image
from pytesseract import *

# 加载图片
image = Image.open(u'test1.jpg')
print(image)
# 识别过程
text = image_to_string(image)
print(text)