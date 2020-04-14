# ---------------------------- bitwise operation in images ----------------------------------------
# filter out and masking me hame bitwise operaation ki need hoti h.

# bitwise opeartion ke shat image ka size same hona chahiye

# frist we make square than we make eclips

import cv2
import numpy as np 

square = np.zeros((300,300),dtype=np.uint8)
cv2.rectangle(square,pt1=(50,50),pt2 = (250,250),thickness= -1,color =255)
cv2.imshow("square",square)
cv2.waitKey()

ellipse = np.zeros((300,300),dtype=np.uint8)
cv2.ellipse(img = ellipse,center =(150,150),axes =(50,50),angle = 0,startAngle = 20,endAngle = 180,color = 255,thickness = -1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey()


#------------------------------------------ so we cheack binary operation ----------------------------------------------------------
# frist iamge and 2nd image ke 1 - 1 pixel  ki operation perform honge
B_and = cv2.bitwise_and(square,ellipse)   # jo jo match hoga vahi show hoga
cv2.imshow("B_and",B_and)
cv2.waitKey()


B_or = cv2.bitwise_or(square,ellipse)   # jo jo match hoga vahi show hoga
cv2.imshow("B_or",B_or)
cv2.waitKey()


B_xor = cv2.bitwise_xor(square,ellipse)   # jo jo match hoga vahi show hoga
cv2.imshow("B_xor",B_xor)
cv2.waitKey()

B_not = cv2.bitwise_not(ellipse)   # jo jo match hoga vahi show hoga
cv2.imshow("B_not",B_not)
cv2.waitKey()

cv2.destroyAllWindows()