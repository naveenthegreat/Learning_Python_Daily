import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize
    resized = cv2.resize(frame, (640, 480))

    # Rotate (90 degrees)
    rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)

    # Flip (0 = vertical, 1 = horizontal)
    flipped = cv2.flip(resized, 1)

    # Show all three
    cv2.imshow("Original", frame)
    cv2.imshow("Rotated", rotated)
    cv2.imshow("Flipped", flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
