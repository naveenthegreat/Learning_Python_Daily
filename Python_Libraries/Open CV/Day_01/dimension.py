import cv2
image = cv2.imread(r"Learning_Python_Daily/Python_Libraries/Open CV/Day_01/pokemon.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Height:{h}\nWeight:{w}\nColor:{c}")

else:
    print("Image is not loaded properly")