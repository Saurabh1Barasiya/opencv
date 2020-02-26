# hare we split all the plane of RGB
# and merge alll images
import cv2
img = cv2.imread(r"F:\python_prog\learn_open_cv\Lenna.png") 
cv2.imshow("Original_image",img)

# --------------so here we split the image-----------------------------

# split function list return karega
print(type(cv2.split(img)))
# print(cv2.split(img))
B,G,R = cv2.split(img)
blue = cv2.imshow("Blue",B)
green = cv2.imshow("Green",G)
red = cv2.imshow("Red",R)

#-------------- hare we merge the images----------------------------
merge = cv2.merge([B,G,R])
cv2.imshow("merge_image",merge)

# --------------if i want only red,blue,green image so ------------------
cv2.imshow("Red_image",cv2.merge([B*0,G*0,R]))
cv2.imshow("Blue_image",cv2.merge([B,G*0,R*0]))
cv2.imshow("Green_image",cv2.merge([B*0,G,R*0]))

cv2.waitKey(0)

# ----------thoda bhut change karna h to ------------------------------

cv2.imshow("Red_image",cv2.merge([B*0,G*0,R+20]))
cv2.waitKey(0)
cv2.imshow("Blue_image",cv2.merge([B+50,G*0,R*0]))
cv2.waitKey(0)
cv2.imshow("Green_image",cv2.merge([B*0,G+60,R*0]))
cv2.waitKey(0)


cv2.destroyAllWindows()