# -------------------------------- camera using canny -------------------------------------------
import cv2
import numpy as np 


def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edge = cv2.Canny(img_gray_blur,threshold1 = 10,threshold2 = 70)
    # thresholding gray_scale ko binary me convert karega
    ret,mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    return mask

cap = cv2.VideoCapture(0)
while True:
   ret , frame = cap.read()
#    cv2.imshow("Frame",frame)
   cv2.imshow("Live Sketch1",frame)
   cv2.imshow("Live Sketch2",sketch(frame))
   if cv2.waitKey(1)== 13: # enter
       break

cap.release()
cv2.destroyAllWindows()