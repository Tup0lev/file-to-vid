from PIL import Image
from PIL import Image
import numpy as np
import binascii
import math

im = Image.open('output.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
print(pixel_values)
px = ""
for tup in pixel_values:
    for dec in tup:
        dec = str(hex(dec)).replace("0x","")
        if (len(dec) == 1):
            dec = "0" + dec
        px = px + dec
print(px)

px = px.rstrip("0")
if (len(px) % 2) != 0:
    px = px + "0"
print(px)
print(len(px))
fp = open("asdfghjkl", "wb+")
fp.write(binascii.unhexlify(px))
fp.close()
