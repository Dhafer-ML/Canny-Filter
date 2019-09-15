import cv2
cap=cv2.VideoCapture(0)
while 1:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY )
    edge=cv2.Canny(gray,50,50)
    cv2.imshow('cany_detector',edge)
    cv2.imshow('orginal', img)
    cv2.waitKey(10)
cap.release()
cv2.destroyAllWindows()