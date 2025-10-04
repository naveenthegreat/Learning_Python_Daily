import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Day_02\pokemon.jpg")

if image is not None:
    print("Image loaded successfully")
    (h,w) = image.shape[:2]
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original",image)
    cv2.imshow("Rotated",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded successfully")