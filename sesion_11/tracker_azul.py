import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Hue Saturation Brightness
    lower_blue = np.array([-10, 50, 50])
    upper_blue = np.array([20, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_not(img, img, mask=mask)

    cv2.imshow("frame", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(img.shape)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()