import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Day_01\pokemon.jpg")
    
if image is not None:
     cv2.imshow("pokemon.jpg",image)        # open the window
     cv2.waitKey(0)                         # wait for key
     cv2.destroyAllWindows()                # close the window
else :
     print("Image not load properly")