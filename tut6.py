#------------------how to genrate background----------------------
# bina background ke hm kuch likh nahi  sakte
import cv2
import numpy as np 
img = np.zeros((512,512),dtype = np.uint8)
cv2.imshow("black",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------- if i want white image-------------------
img1 =255 + (np.zeros((512,512),dtype = np.uint8))
cv2.imshow("White",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ------------------cheak or koi color aata h kya----------------
img2 =100 + (np.zeros((512,512),dtype = np.uint8))
cv2.imshow("cheack",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
       # changes ho rahe h background me
