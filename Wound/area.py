# -*- coding: utf-8 -*-
"""area.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12InV13NA6DOXf7JFgAJBJnAPTHEzSqoS
"""

import numpy as np
from PIL import Image

src = np.array(Image.open('data1/src/lena.jpg'))
mask = np.array(Image.open('data1/src/horse_r.jpg').resize(src.shape[1::-1], Image.BILINEAR))

# uint8 0 255

mask = mask / 255

# float64 0.0 1.0

dst = src * mask

Image.fromarray(dst.astype(np.uint8)).save('data1/dst/numpy_image_mask.jpg')

# ![](data1/dst/numpy_image_mask.jpg)

mask = np.array(Image.open('data1/src/horse_r.jpg').convert('L').resize(src.shape[1::-1], Image.BILINEAR))


# (225, 400)

mask = mask / 255

# dst = src * mask
# ValueError: operands could not be broadcast together with shapes (225,400,3) (225,400) 

# mask = mask[:, :, np.newaxis]

mask = mask.reshape(*mask.shape, 1)

# (225, 400, 1)

dst = src * mask






# ![](data1/dst/numpy_image_mask_l.jpg)

import numpy as np
from PIL import Image
import cv2
img1 = cv2.imread('data1/src/horse_r.jpg')
dest_not1 = cv2.bitwise_not(img1, mask = None)
cv2.imwrite('data1/src/horse1.jpg',dest_not1)
import numpy as np
from PIL import Image

src = np.array(Image.open('data1/src/lena.jpg'))
mask = np.array(Image.open('data1/src/horse1.jpg').resize(src.shape[1::-1], Image.BILINEAR))

# uint8 0 255

mask = mask / 255

# float64 0.0 1.0

dst = src * mask

Image.fromarray(dst.astype(np.uint8)).save('data1/dst/numpy_image_mask2.jpg')

# ![](data1/dst/numpy_image_mask.jpg)

mask = np.array(Image.open('data1/src/horse1.jpg').convert('L').resize(src.shape[1::-1], Image.BILINEAR))

# (225, 400)

mask = mask / 255

# dst = src * mask
# ValueError: operands could not be broadcast together with shapes (225,400,3) (225,400) 

# mask = mask[:, :, np.newaxis]

mask = mask.reshape(*mask.shape, 1)

# (225, 400, 1)

dst = src * mask





# ![](data1/dst/numpy_image_mask_l.jpg)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy

def correlate(mask, surrounding):
  mask = mask.astype('float')
  surrounding = surrounding.astype('float')
  mask[mask == 0] = numpy.nan
  surrounding[surrounding == 0] = numpy.nan
  avg_color_per_row_masked = numpy.nanmean(mask, axis=0)
  avg_color_masked = numpy.nanmean(avg_color_per_row_masked, axis=0)
  avg_color_per_row_surrounding = numpy.nanmean(surrounding, axis=0)
  avg_color_surrounding = numpy.nanmean(avg_color_per_row_surrounding, axis=0)
  measurement = abs(numpy.log(avg_color_masked/avg_color_surrounding))
  print(numpy.mean(measurement))
  return (numpy.mean(measurement))


masked_part = cv2.imread('data1/dst/numpy_image_mask.jpg')
unmasked_part = cv2.imread('data1/dst/numpy_image_mask2.jpg')
correlate(masked_part, unmasked_part)