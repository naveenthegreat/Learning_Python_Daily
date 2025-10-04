import cv2
image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Image\Day_02\pokemon.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Height:{h}\nWidth:{w}\nColor:{c}")

else:
    print("Image is not loaded properly")