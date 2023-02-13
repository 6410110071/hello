def grade_calculator(points_earned, points_possible):
    percentage = 100 * (points_earned / points_possible)
    return percentage

def determine_letter_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

points_earned = float(input("Enter the number of points earned: "))
points_possible = float(input("Enter the total number of points possible: "))

percentage = grade_calculator(points_earned, points_possible)
letter_grade = determine_letter_grade(percentage)

print("Your grade is: {:.2f}% ({})".format(percentage, letter_grade))
