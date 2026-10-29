
# Student App Access Manager

# Approved and restricted apps
approved_apps = ["classroom", "dictionary", "calculator"]
restricted_apps = ["gaming", "social media", "video"]

app_name = input("Enter the app name: ").lower()
student_age = int(input("Enter your age: "))

# Check data types
print("\n--- Data Type Check ---")
print("App name type:", type(app_name))
print("Age type:", type(student_age))

# Check app access
print("\n--- App Access Check ---")

if app_name in approved_apps:
    print("App is approved. Access allowed.")

elif app_name in restricted_apps:
    print("App is restricted. Access denied.")

else:
    print("App is not listed. Ask a teacher for approval.")

# Represent permissions using binary values
READ = 1       # Binary: 001
WRITE = 2      # Binary: 010
PLAY = 4       # Binary: 100

permissions = READ | PLAY

print("\n--- Permission Check ---")
print("Permission value:", permissions)
print("Binary permissions:", bin(permissions))

# Test individual permissions
print("Can read:", bool(permissions & READ))
print("Can write:", bool(permissions & WRITE))
print("Can play:", bool(permissions & PLAY))

# Remove PLAY permission
permissions = permissions & ~PLAY
print("Permissions after removing PLAY:", permissions)

# Demonstrate bit shifts
print("\n--- Bit Shift Demo ---")
number = 4

print("Original number:", number)
print("Left shift by 1:", number << 1)
print("Right shift by 1:", number >> 1)
