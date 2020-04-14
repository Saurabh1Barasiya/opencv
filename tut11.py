# ----------------------------- Here we crop the image -----------------------------------

import cv2
import numpy as np 

img = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png')
cv2.imshow("image",img)
print(img.shape)
height,width = img.shape[0:2]
print(height,width)
cv2.waitKey()

# if we have start and end point so we crop the image

start_row , start_col = int(height * 0.25) , int(width * 0.25) # here we find x1 , y1
print(start_row,start_col)

end_row , end_col = int(height * 0.75) , int(width * 0.75) # here we find x2 , y2
print(end_col,end_row)

crop = img[start_row : end_row,start_col : end_col]
cv2.imshow("Crop",crop)

cv2.waitKey()
cv2.destroyAllWindows()