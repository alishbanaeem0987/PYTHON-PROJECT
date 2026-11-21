
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "Grade A"
elif marks >= 80:
    grade = "Grade B"
elif marks >= 70:
    grade = "Grade C"
elif marks >= 60:
    grade = "Grade D"
else:
    grade = "Fail"

print("Your grade is:", grade)
