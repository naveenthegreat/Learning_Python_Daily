import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Image\Day_02\pokemon.jpg")

if image is not None:
    print("Image loaded Successfully")
    cv2.putText(image,"Hello N.K.Nayak k fans",(50,80),
                cv2.FONT_HERSHEY_COMPLEX,1.2,(0,235,230),3)

    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")