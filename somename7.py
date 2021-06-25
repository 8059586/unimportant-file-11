import cv2
def takeSnapshot():
    videoCapture = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = videoCapture.read()
        cv2.imwrite("Hello.png",frame)
        result = False
    videoCapture.release()
    cv2.destroyAllWindows()
takeSnapshot()