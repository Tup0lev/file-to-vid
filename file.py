from PIL import Image
import numpy as np
import binascii
import math
a = ""
matrix = []
with open('asdf.txt', 'rb') as f:
    for chunk in iter(lambda: f.read(3), b""):
    #    print (binascii.hexlify(chunk))
        hex = str(binascii.hexlify(chunk))
        hex = hex[1:]
        hex = hex.replace("'", "")
        #create a tuple
        a = a + hex
        print(hex)
        while(len(hex)<6):
            hex = hex + "0"
            print(hex)
        tup = (int(hex[0:2],16),int(hex[2:4],16),int(hex[4:],16))
        matrix.append(tup)
        print(tup)
   #     asdf = (binascii.hexlify(chunk))
print(len(matrix))

while ((float(np.sqrt(len(matrix))).is_integer()) == False):
	matrix.append( (0,0,0) )
	
img_size = int(np.sqrt(len(matrix)))
array = np.array([matrix[img_size*i:img_size*(i+1)] for i in range(img_size)], dtype=np.uint8)

img = Image.fromarray(array)
print(a)
img.save('output.png')

