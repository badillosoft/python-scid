import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # line(img, coord_ini, coord_fin, color, width)
    img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    # Display the resulting frame
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()