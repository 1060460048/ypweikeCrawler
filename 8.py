# -*- coding: utf-8 -*-

import os
import sys
from pytesser import *
from PIL import Image

reload(sys)
sys.setdefaultencoding( "utf-8" )

os.chdir('D:\\Python27\\Lib\\site-packages')

image=Image.open(r'D:\\Download\\pic\\600.jpg')
print image

print image_to_string(image)
print image_file_to_string('D:/Download/1.jpg')
