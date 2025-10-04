import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Image\Day_02\pokemon.jpg")

if image is not None:
    cropped = image[490:500,300:600]
    cv2.imshow("Original",image)
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded")