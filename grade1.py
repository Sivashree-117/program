marks = float(input("Enter student marks: "))

if marks >= 95:
    grade = "A+"
elif marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"
with open("grade_output.txt", "a") as file:
    print(f"Marks: {marks}", file=file)
    print(f"Grade: {grade}", file=file)
    print("-" * 30, file=file)

print("Grade stored in grade_output.txt")
