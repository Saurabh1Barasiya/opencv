# how to convert iamge RGB to grayscale
# ham diect RGB se binary me convert nahi kar sakte iske liye hame 3 steps ki need hogi
# hamare system par COLOR reverse me store hote h  RGB --> BGR

import cv2
import numpy as np
img = cv2.imread(r"F:\python_prog\learn_open_cv\Lenna.png") 

gray_scale =  cv2.cvtColor(src = img,code = cv2.COLOR_BGR2GRAY) # image ko convert karne ke liye
cv2.imshow("leena",img)
cv2.imshow("gray",gray_scale)

# ab hame image ko binary means black and white me convert karna h 
ret,bin_i = cv2.threshold(src=gray_scale,thresh = 126,maxval = 255,type =cv2.THRESH_BINARY)
print("threhvalue",ret)
cv2.imshow("binry_iamge",bin_i)

# so if we cheack the dimension of images
print("RGB image shape",img.shape)

print("grayscale image shape",gray_scale.shape)

print("binary image shape",bin_i.shape)

# if you want to save these imagess so you need to imwrite function
cv2.imwrite(r"F:\python_prog\learn_open_cv\LEENA_RGB.jpg",img)
cv2.imwrite(r"F:\python_prog\learn_open_cv\LEENA_GRAY_SCALE.jpg",gray_scale)
cv2.imwrite(r"F:\python_prog\learn_open_cv\LEENA_BINARY.jpg",bin_i)
print("ALL files write sucessfully")
cv2.waitKey(0)
cv2.destroyAllWindows()