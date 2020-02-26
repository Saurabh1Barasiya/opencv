# here we cheack image shape 
# how to write image
import cv2
import numpy as np
img = cv2.imread(r"F:\python_prog\learn_open_cv\Lenna.png") # image  ko read kiya
print(img.shape)  # it gives me shape of image height width and depth
h,w,d = img.shape
print(f" heihgt of image is {h} \n width of an iamge is {w} \n depth of iamge is {d}")
cv2.imshow("leena",img)  # show karne ke liyes
cv2.waitKey(2000)  # image ko 5 secound me band kar dega

# ------------------------image writhing----------------------------------
cv2.imwrite(r"F:\python_prog\learn_open_cv\output.jpg",img)

cv2.destroyAllWindows()
h1,w1,d1 = np.shape(img)
print(f" heihgt of image is {h1} \n width of an iamge is {w1} \n depth of iamge is {d1}")

# ------------------------here we cheack datatype----------------------------
print(type(img))
print(img.dtype)  # uint8    unsignd integer of 8 bit  = 2^8 = 256 ===  0--255
