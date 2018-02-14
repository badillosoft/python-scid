import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # line(img, coord_ini, coord_fin, color, width)
    pts = np.array([[640, 480], [700, 480],[700, 420],[640, 420]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255), 5)

    # Display the resulting frame
    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(img.shape)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()