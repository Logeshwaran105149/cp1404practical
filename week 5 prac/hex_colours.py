COLOR_NAME_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Blue": "#0018a8"
}
print(COLOR_NAME_TO_CODE)
Color_name = input("Enter name of the color: ")
while Color_name != "":
    try:
        if Color_name in COLOR_NAME_TO_CODE:
            print(COLOR_NAME_TO_CODE[Color_name])
            Color_name = input("Enter name of the color: ")
        else:
            print("Invalid color name")
    except KeyError:
        print("An error occurred:")
