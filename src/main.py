
from calculator import calculator
from unit_converter import unit_converter
from gpa_calculator import gpa_calculator
from quiz import quiz
from input_validation import input_validation_demo


def main():
    while True:
        print("\n========== TEAM TOOLKIT ==========")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. GPA Calculator")
        print("4. Quiz")
        print("5. Input Validation Demo")
        print("6. Exit")
        print("==================================")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                calculator()

            elif choice == 2:
                unit_converter()

            elif choice == 3:
                gpa_calculator()

            elif choice == 4:
                quiz()

            elif choice == 5:
                input_validation_demo()

            elif choice == 6:
                print("Thank you for using Team Toolkit!")
                break

            else:
                print("Invalid choice! Please select 1-6.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
