
# Enter three speeds
a = float(input("Enter first speed: "))
b = float(input("Enter second speed: "))
c = float(input("Enter third speed: "))

# Calculate average
avg = (a + b + c) / 3

print("Average speed:", avg)

# Compare average with the three speeds
if avg > a and avg > b and avg > c:
    print("Average is greater than all three speeds")

elif avg > a and avg > b:
    print("Average is greater than a and b")

elif avg > a and avg > c:
    print("Average is greater than a and c")

elif avg > b and avg > c:
    print("Average is greater than b and c")

elif avg > a:
    print("Average is greater than a")

elif avg > b:
    print("Average is greater than b")

elif avg > c:
    print("Average is greater than c")

else:
    print("invalid input")
