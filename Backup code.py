import cv2
capture = cv2.VideoCapture(0)
while True:
    _,frame = capture.read()
    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)