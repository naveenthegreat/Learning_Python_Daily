import cv2
image = cv2.imread(r"Learning_Python_Daily/Python_Libraries/Open CV/Day_01/naruto.webp")

if image is not None:
    option=input("Enter your location:")
    op1=input("1.Show\n2.Save\n")
    if op1=="1":
        gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("naruto",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif op1=="2":
        gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        choice=input("Save image as :")
        cv2.imwrite(f"{choice}.png",gray)

    else:
        print("Error")

else:
    print("Could not load the image")
