# here we use Camera using cv2 module
# aaski code me 13 means  enter  and 27 means escape
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow("Camera",frame)
    # if cv2.waitKey(1) == 27:
    #     break
    if cv2.waitKey(1) == ord("q"):
        break
cap.release() # resourse ko close kar dega
cv2.destroyAllWindows()  # resourse ko close kar dega