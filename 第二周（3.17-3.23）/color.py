import cv2
import numpy as np

lower_red_0 = np.array([0, 43, 47])
upper_red_0 = np.array([5, 255, 255])
lower_red_1 = np.array([156, 43, 47])
upper_red_1 = np.array([180, 255, 255])
lower_blue = np.array([100, 47, 47])
upper_blue = np.array([124, 255, 255])
lower_green = np.array([35, 43, 47])
upper_green = np.array([77, 255, 255])

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(3, 640)
capture.set(4, 480)

def filter_rbg(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    res_red = np.array([0])
    res_green = np.array([0])
    res_blue = np.array([0])
    if 'red' in color:
        mask_red_0 = cv2.inRange(hsv, lower_red_0, upper_red_0)
        mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
        mask_red = mask_red_1 + mask_red_0
        res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    if 'blue' in color:
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    if 'green' in color:
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    res = cv2.bitwise_or(res_red, res_green)
    res = cv2.bitwise_or(res, res_blue)
    cv2.imshow('result', res)


while (True):
    ref, frame = capture.read()
    filter_rbg(frame, ['red', 'green', 'blue'])
    cv2.imshow("camera", frame)
    
    c = cv2.waitKey(1)
    if c == 27:
        print(frame)
        capture.release()
        break
