
# Swimming Pool Entry Checker

age = int(input("Enter your age: "))
can_swim = input("Can you swim? (yes/no): ").lower()
adult = input("Is an adult supervising you? (yes/no): ").lower()

print("\n===== POOL ENTRY CHECK =====")

# Deep end: swimmer must be at least 12 and able to swim
if age >= 12 and can_swim == "yes":
    print("You may enter the deep end, subject to pool rules.")

# Shallow end: younger swimmers need adult supervision
elif age < 12 and adult == "yes":
    print("You may use the shallow end with adult supervision.")

# Anyone who cannot swim needs supervision and must stay shallow
elif can_swim == "no" and adult == "yes":
    print("You may use the shallow end with adult supervision.")
    print("Do not enter the deep end.")

# No swimming ability and no adult supervision
elif can_swim == "no" and adult == "no":
    print("Entry is not allowed until a responsible adult supervises you.")

# Unknown or unmet conditions
else:
    print("Please ask the lifeguard to check your eligibility.")
    print("Do not enter the pool until approved.")

print("\nAlways follow the lifeguard's instructions.")
