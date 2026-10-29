
# Farm Harvest Calculator

# Harvest from 5 fields in kilograms
field1 = 120
field2 = 150
field3 = 100
field4 = 180
field5 = 200

# Calculate total and average
total = field1 + field2 + field3 + field4 + field5
average = total / 5

# Pack grain into 25 kg bags
bags = total // 25
leftover = total % 25

# Compare with last year's harvest
last_year = 650
difference = total - last_year

print("===== FARM HARVEST REPORT =====")
print("Total harvest:", total, "kg")
print("Average harvest:", average, "kg")
print("25 kg bags:", bags)
print("Leftover grain:", leftover, "kg")
print("Last year's harvest:", last_year, "kg")

if difference > 0:
    print("Harvest increased by", difference, "kg")
elif difference < 0:
    print("Harvest decreased by", abs(difference), "kg")
else:
    print("Harvest is the same as last year")

# Add bonus crop and reserve seeds
bonus_crop = 50
seed_reserve = 75

updated_total = total + bonus_crop
available_grain = updated_total - seed_reserve

print("\n===== UPDATED HARVEST =====")
print("Harvest after bonus:", updated_total, "kg")
print("Grain after seed reserve:", available_grain, "kg")
