amount = int(input("Enter the amount: "))

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_10 = amount // 10
amount = amount % 10

print("500 notes:", notes_500)
print("200 notes:", notes_200)
print("100 notes:", notes_100)
print("50 notes:", notes_50)
print("10 notes:", notes_10)
print("Remaining amount:", amount)