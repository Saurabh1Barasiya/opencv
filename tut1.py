# so we learn opencv
# frist we install opencv
# pip install opencv-python
# pip install opencv-contrib-python  

# ---------------------- start ---------------------------------------
import cv2
img = cv2.imread(r"F:\python_prog\learn_open_cv\Lenna.png")
print(img)
# image hame matrix ke format me mili h to agar hame pic ke format me dekhna h to hm imshow() ka use karege
cv2.imshow("Leena",img)
# cv2.waitKey(2000)  # here 2000 means 2 mili secound

# if you want to open your pic always so 
cv2.waitKey(0)
cv2.destroyAllWindows()   # sarae resourse ko close  kar dega