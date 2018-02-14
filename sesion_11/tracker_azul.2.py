import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Hue Saturation Brightness
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    max_cnt = None
    max_area = -1

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if max_area < area:
            max_cnt = cnt

    M = cv2.moments(max_cnt)

    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        img = cv2.circle(img, (cx, cy), 50, (255, 255, 0), 4)

    cv2.imshow("frame", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(img.shape)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()