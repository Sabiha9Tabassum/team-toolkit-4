
def get_valid_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_valid_choice(message, min_value, max_value):
    while True:
        try:
            choice = int(input(message))

            if min_value <= choice <= max_value:
                return choice
            else:
                print("Invalid choice! Please select a valid option.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def input_validation_demo():
    print("\n--- Input Validation Demo ---")

    number = get_valid_number("Enter a number: ")
    print("Valid number:", number)

    choice = get_valid_choice("Choose a number (1-4): ", 1, 4)
    print("Valid choice:", choice)


if __name__ == "__main__":
    input_validation_demo()
