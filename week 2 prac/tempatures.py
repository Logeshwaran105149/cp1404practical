menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(menu)
    user_choice()
    convert_celsius_fahrenheit()
    convert_fahrenheit_celsius()


def convert_celsius_fahrenheit():
    celsius = float(input("celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_fahrenheit_celsius():
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def user_choice():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
