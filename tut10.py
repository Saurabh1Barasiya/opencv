# -------------------   how to resize image   ----------------------------
import cv2
import numpy as np

img = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png')
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()

# ------------ if you want to direct convert grayscale ----------------------
gray_img = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png',0)
cv2.imshow("gray_iamge",gray_img)
cv2.waitKey()
cv2.destroyAllWindows()

#------------------------- resize image---------------------------
img1 = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png')
cv2.imshow("image",img1)
cv2.waitKey()

resize = cv2.resize(img1,dsize=None,fx =0.50,fy=0.50)
cv2.imshow("resize",resize)
cv2.waitKey()



# --------------------if you  want to double your image--------------------------
img1 = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png')
cv2.imshow("image",img1)
cv2.waitKey()

resize_double = cv2.resize(img1,dsize=None,dst=None,fx =2,fy=2)
cv2.imshow("resize_double",resize_double)
cv2.waitKey()


#------------------------ direct resize --------------------------------------------------

img4 = cv2.imread(r'F:\python_prog\learn_open_cv\Lenna.png')
cv2.imshow("image_4",img4)
cv2.waitKey()

resize_squad = cv2.resize(img1,(200,200))
cv2.imshow("resize_squad",resize_squad)
cv2.waitKey()


cv2.destroyAllWindows()