import cv2
import numpy as np

yellow = [0, 255, 255]  # yellow in bgr
c = np.uint8([[yellow]])  # the bgr values which you want to convert to hsv
hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
lowerLimit = hsvC[0][0][0] - 10, 100, 100
upperLimit = hsvC[0][0][0] + 10, 255, 255
lowerLimit = np.array(lowerLimit, dtype=np.uint8)
upperLimit = np.array(upperLimit, dtype=np.uint8)
video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    HSVimage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSVimage, lowerLimit, upperLimit)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)



    cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
    cv2.namedWindow("webcam", cv2.WINDOW_NORMAL)
    cv2.imshow("mask", mask)
    cv2.imshow("webcam", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
