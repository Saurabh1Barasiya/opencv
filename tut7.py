#-------------------how to draw  ciccle ,line,rectangle..--------------------
import cv2
import numpy as np 
img = np.zeros((512,512,3),dtype = np.uint8)
img1 = np.zeros((512,512,3),dtype = np.uint8)
cv2.imshow("black",img)
cv2.waitKey(0)
cv2.imshow("Line",cv2.line(img=img,pt1 = (0,0),pt2 = (511,511),color = (250,0,0),thickness = 5))
cv2.waitKey(0)
cv2.imshow("New_line",cv2.line(img=img1,pt1 = (0,0),pt2 = (511,511),color = (0,0,250),thickness = 5))
cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------------------------------------------------------------------------------------------------------
# we create rectangle 
img3 = np.zeros((512,512,3),dtype = np.uint8)
cv2.imshow("rectangle",cv2.rectangle(img = img3,pt1 = (100,100),pt2 = (300,300),color = (200,210,60),thickness = -5))
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------
# we want create  circle
img4 = np.zeros((512,512,3),dtype = np.uint8)
cv2.imshow("Circle",cv2.circle(img = img4,center=(300,300),radius = (50),color = (200,210,60),thickness = -5))
cv2.waitKey(0)
cv2.destroyAllWindows()


#----------------------------------------------------------------------------------------------------------
# here we create polygone
#--------------------------------------------------------------------------------------------
# we want create  circle
img5 = np.zeros((512,512,3),dtype = np.uint8)
pts = np.array([[10,30],[40,50],[100,150],[300,250]])
cv2.imshow("Circle",cv2.polylines(img = img5,pts = [pts],color = (200,210,60),isClosed = True,thickness = 5))
cv2.waitKey(0)
cv2.destroyAllWindows()




