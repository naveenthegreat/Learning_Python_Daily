import cv2
image = cv2.imread(r"Learning_Python_Daily/Python_Libraries/Open CV/Day_01/pokemon.jpg")

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image could not be loaded")