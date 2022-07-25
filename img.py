from PIL import Image
import numpy as np

long_list = [(255, 255, 255), (0, 0, 0) , (0, 0, 0)]
img_size = 1
array = np.array([long_list[img_size*i:img_size*(i+1)] for i in range(img_size)], dtype=np.uint8)

img = Image.fromarray(array)

img.save('output.png')
