# how to add test in img
import cv2
import numpy as np 
img = np.zeros((512,512,3),dtype=np.uint8)
cv2.putText(img = img,text = "Sauarabh",org=(10,290),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 2,color = (120,145,40),thickness = 5)
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
