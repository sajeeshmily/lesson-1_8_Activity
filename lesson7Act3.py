
# Student Grade Calculator

marks = []

for i in range(1, 6):
    mark = int(input("Enter marks for subject " + str(i) + ": "))

    if mark not in range(0, 101):
        print("Invalid marks! Enter marks between 0 and 100.")
        break

    marks.append(mark)

if len(marks) == 5:
    average = sum(marks) / 5

    print("\nTotal marks:", sum(marks))
    print("Average marks:", average)

    if average in range(91, 101):
        print("Grade: A+")

    elif average in range(81, 91):
        print("Grade: A")

    elif average in range(71, 81):
        print("Grade: B")

    elif average in range(61, 71):
        print("Grade: C")

    elif average in range(51, 61):
        print("Grade: D")

    else:
        print("Grade: F")
