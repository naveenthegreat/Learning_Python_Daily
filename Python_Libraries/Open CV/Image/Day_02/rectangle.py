import cv2

image = cv2.imread(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Open CV\Image\Day_02\pokemon.jpg")

if image is not None:
    print("Image loaded Successfully")
    pt1=(50,100)
    pt2=(200,350)
    color=(0,240,0)
    thickness=4
    pt=(220,380)
    ptt=(20,150)
    colorr=(0,240,0)
    thicknesss=4

    # ok = cv2.line(image,pt1,pt2,color,thickness)
    ok2 = cv2.rectangle(image,pt,ptt,colorr,thicknesss)
    # cv2.imshow("Image with line",ok)
    cv2.imshow("Image with line",ok2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")