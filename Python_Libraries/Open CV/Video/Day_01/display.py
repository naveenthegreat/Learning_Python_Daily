import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 3)
    cv2.imshow("Live",frame)
    cv2.imshow("Gray",gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()