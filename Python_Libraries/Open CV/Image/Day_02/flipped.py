import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Day_02\pokemon.jpg")

if image is not None:
    print("Image loaded successfully")
    flipped_horizontally = cv2.flip(image,1)
    flipped_vertically = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("Original",image)
    cv2.imshow("Horizontal",flipped_horizontally)
    cv2.imshow("Vertical",flipped_vertically)
    cv2.imshow("Both",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded successfully")