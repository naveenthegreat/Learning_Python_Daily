import cv2
image = cv2.imread(r"Learning_Python_Daily/Python_Libraries/Open CV/Day_01/pokemon.jpg")

if image is not None:
    success = cv2.imwrite("output_pokemon.png",image)
    if success:
        print("The changed file saved as 'output_pokemon.png'")

    else :
        print("The changed file is not as 'output_pokemon.png'")

else:
    print("Error:could not load the image")