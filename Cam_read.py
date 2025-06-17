import cv2 as cv
camid=0
cam = cv.VideoCapture(camid)
while True:
    status, frame = cam.read() 
    if status==True:
     cv.imshow('Your cam', frame)  
    if cv.waitKey(1) == ord('q'): 
        break

cam.release()
cv.destroyAllWindows()