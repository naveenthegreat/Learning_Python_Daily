import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Day_02\pokemon.jpg")

if image is not None:
    print("Image Loaded")
    resized = cv2.resize(image,(400,400))
    cv2.imshow("Original_Photo",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Resized_photo",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded successfully")

