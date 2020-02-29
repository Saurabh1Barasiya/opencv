# --------------------------------- mouse handling event ----------------------------------------------
import cv2
import numpy as np
img = np.zeros((512,512,3),dtype=np.uint8)
window = "win"

cv2.namedWindow(window)

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imshow("circle",cv2.circle(img,(x,y),20,(255,0,0),-1))
        
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.imshow("circle",cv2.circle(img,(x,y),10,(20,45,10),-1))
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imshow("circle",cv2.circle(img,(x,y),30,(20,45,10),-1))
    if event == cv2.EVENT_MBUTTONDBLCLK:
        cv2.imshow("circle",cv2.circle(img,(x,y),20,(255,0,0),-1))

cv2.setMouseCallback(window,draw)
while True:
    cv2.imshow(window,img)
    cv2.waitKey(0)
cv2.destroyAllWindows()