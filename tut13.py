 # ------------------------------- technique of edge dection -------------------------------------------
 # color flirting ke uper iska use hota h

 # 1. sobal 
 # 2. lablacian
 # 3. Canny


# edge dection ke liye apko sabse pahle image ko gray sacle me convert korna hota h
import cv2
import numpy as np

img = cv2.imread(r"F:\python_prog\learn_open_cv\Lenna.png",0)
cv2.imshow("img",img)
cv2.waitKey(0)

# sobal alag alag axis par image ko scane karta h
height,width = img.shape
sobal_x = cv2.Sobel(img,ddepth = cv2.CV_64F,dx = 1,dy = 0,ksize=5)
sobal_y = cv2.Sobel(img,ddepth = cv2.CV_64F,dx = 0,dy = 1,ksize=5)
cv2.imshow("Sobal_x",sobal_x)
cv2.waitKey(0)
cv2.imshow("Sobal_y",sobal_y)
cv2.waitKey(0)


# ---------------------Laplacian----------------------------------

lap = cv2.Laplacian(img,ddepth = cv2.CV_64F)
cv2.imshow("Laplacian",lap)
cv2.waitKey(0)



# ----------------------------- Canny --------------------------------------
canny = cv2.Canny(img,threshold1 = 0,threshold2 = 200)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
