
def gpa_calculator():
    print("\n--- GPA Calculator ---")

    try:
        total_courses = int(input("Enter number of courses: "))

        if total_courses <= 0:
            print("Please enter a valid number of courses.")
            return

        total_points = 0
        total_credits = 0

        for i in range(total_courses):
            print("\nCourse", i + 1)

            grade_point = float(input("Enter grade point (0.0-4.0): "))
            credit = float(input("Enter course credit: "))

            if not 0 <= grade_point <= 4:
                print("Invalid grade point!")
                return

            if credit <= 0:
                print("Credit must be greater than zero!")
                return

            total_points += grade_point * credit
            total_credits += credit

        gpa = total_points / total_credits

        print("\nYour GPA is:", round(gpa, 2))

    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    gpa_calculator()
