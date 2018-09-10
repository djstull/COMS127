score = int(input("Enter the student's score: "))
grade = ("F")
if score >= 60:
    grade = ("C")
if score >= 80:
    grade = ("B")
if score >= 90:
    grade = ("A")
print("Letter Grade:" + str(grade))