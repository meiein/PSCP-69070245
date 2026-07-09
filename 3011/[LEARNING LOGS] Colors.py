"""[LEARNING LOGS] Colors"""

color1 = {"Red", "Yellow", "Blue"}
color2 = {"Red", "Yellow", "Blue"}

color1 = input()
color2 = input()
if color1 == "Red" and color2 == "Yellow":
    print("Orange")
elif color1 == "Red" and color2 == "Blue":
    print("Violet")
elif color1 == "Yellow" and color2 == "Blue":
    print("Green")
elif color2 == "Red" and color1 == "Yellow":
    print("Orange")
elif color2 == "Red" and color1 == "Blue":
    print("Violet")
elif color2 == "Yellow" and color1 == "Blue":
    print("Green")
elif color1 == "Red" and color2 == "Red":
    print("Red")
elif color1 == "Blue" and color2 == "Blue":
    print("Blue")
elif color1 == "Yellow" and color2 == "Yellow":
    print("Yellow")
else:
    print("Error")
    