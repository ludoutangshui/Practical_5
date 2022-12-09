CODE_TO_NAME = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                "Apricot": "#fbceb1", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "Antique White": "#faebd7", "Antique White1": "#ffefdb", "Antique White2": "#eedfcc"}

choice = input("Enter the name: ").title()

while choice != "":
    if choice in CODE_TO_NAME:
        print(CODE_TO_NAME[choice])
    else:
        print("Invalid input")

    choice = input("Enter the name: ").title()

print("See you next time")
