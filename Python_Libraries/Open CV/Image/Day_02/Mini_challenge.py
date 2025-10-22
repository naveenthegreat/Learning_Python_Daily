import cv2

user = input("Add your file: ")
image = cv2.imread(f"{user}")

choice = int(input("What operations to perform on the given file:\n1. Draw a Line" \
"\n2. Draw a Trianlge\n3. Draw a Circle\n4. Add text on the image"))

color = (0,250,235)

if choice==1:
    c1 = int(input("Point 1 (x1): (y1):"))
    c2 = int(input("Point 2 (x2):"&"(y2):"))
    c3 = cv2.line(image,c1,c2,color,4)

elif choice==2:
    c1 = input("Point 1 (x1,y1):")
    c2 = input("Point 2 (x2,y2):")
    c113 = cv2.rectangle(image,c1,c2,color,4)

elif choice==3:
    c6 = input("Point 1 (x1,y1):")
    c7 = input("Radius")
    c13 = cv2.line(image,c6,c7,color,4)

elif choice==4:
    c8 = input("Add Text:\n")
    c12 = input("Origin (x,y):")
    c13 = cv2.line(image,c8,c12,color,cv2.FONT_HERSHEY_SIMPLEX,2,color,4)

else:
    print("Please coice an option")

cv2.imshow("User_image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()