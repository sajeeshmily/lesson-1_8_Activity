
# Grocery Cost Comparison Tool

print("===== GROCERY COST COMPARISON =====")

# Part 1: Operator precedence
rice = float(input("Enter rice cost: "))
milk = float(input("Enter milk cost: "))
vegetables = float(input("Enter vegetable cost: "))
discount = float(input("Enter discount amount: "))

total = (rice + milk + vegetables) - discount
print("\n1. Total grocery cost:", total)

# Part 2: Divisibility using modulus
divisor = int(input("\nEnter a number to check bill divisibility: "))

if divisor != 0:
    if total % divisor == 0:
        print("The bill is divisible by", divisor)
    else:
        print("The bill is not divisible by", divisor)
else:
    print("Cannot divide by zero.")

# Part 3: Correct a wrongly calculated average
wrong_average = float(input("\nEnter the calculated average cost: "))
wrong_cost = float(input("Enter the wrong item cost: "))
correct_cost = float(input("Enter the correct item cost: "))
item_count = int(input("Enter the number of items: "))

if item_count > 0:
    original_sum = wrong_average * item_count
    corrected_sum = original_sum - wrong_cost + correct_cost
    corrected_average = corrected_sum / item_count

    print("Corrected average item cost:", corrected_average)
else:
    print("Item count must be greater than zero.")
    corrected_average = None

# Part 4: Compare this bill with three other bills
bill_a = float(input("\nEnter first family's bill: "))
bill_b = float(input("Enter second family's bill: "))
bill_c = float(input("Enter third family's bill: "))

average_bill = (bill_a + bill_b + bill_c) / 3

print("\nAverage of the three bills:", average_bill)

if total > bill_a and total > bill_b and total > bill_c:
    print("Our bill is higher than all three bills.")
elif total > bill_a and total > bill_b:
    print("Our bill is higher than the first and second bills.")
elif total > bill_a and total > bill_c:
    print("Our bill is higher than the first and third bills.")
elif total > bill_b and total > bill_c:
    print("Our bill is higher than the second and third bills.")
elif total > bill_a:
    print("Our bill is higher than the first bill.")
elif total > bill_b:
    print("Our bill is higher than the second bill.")
elif total > bill_c:
    print("Our bill is higher than the third bill.")
else:
    print("Our bill is not higher than any of the three bills.")

# Final summary
print("\n===== FINAL SUMMARY =====")
print("Our grocery bill:", total)
print("Average comparison bill:", average_bill)

if corrected_average is not None:
    print("Corrected average item cost:", corrected_average)
