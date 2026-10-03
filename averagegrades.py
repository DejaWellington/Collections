def letterGrade (average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    studentName = input("Enter the student name: ")

    grades = []
    grades.append(float(input("Enter a grade: ")))
    grades.append(float(input("Enter a grade: ")))
    grades.append(float(input("Enter a grade: ")))
    grades.append(float(input("Enter a grade: ")))
    grades.append(float(input("Enter a grade: ")))

    average = sum(grades) / len(grades)
    grade = letterGrade(average)

    print()
    print(studentName)
    print(f"Average: {average:g}")
    print("Letter Grade:", grade)

main()
