import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    px = img[640:400, 720:480]

    img[320:160, 400:240] = px

    # Display the resulting frame
    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(img.shape)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()