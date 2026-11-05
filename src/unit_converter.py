
def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Kilograms to Grams")
    print("4. Grams to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")

    choice = input("Choose a conversion (1-6): ")

    try:
        value = float(input("Enter the value: "))

        if choice == "1":
            print("Result:", value * 1000, "meters")

        elif choice == "2":
            print("Result:", value / 1000, "kilometers")

        elif choice == "3":
            print("Result:", value * 1000, "grams")

        elif choice == "4":
            print("Result:", value / 1000, "kilograms")

        elif choice == "5":
            result = (value * 9/5) + 32
            print("Result:", result, "°F")

        elif choice == "6":
            result = (value - 32) * 5/9
            print("Result:", result, "°C")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    unit_converter()
