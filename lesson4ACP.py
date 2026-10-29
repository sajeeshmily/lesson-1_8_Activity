
# Classroom Points Calculator

# Points earned by 5 teams
team1 = 80
team2 = 90
team3 = 70
team4 = 100
team5 = 60

# Calculate total and average points
total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("===== CLASSROOM POINTS =====")
print("Total points:", total)
print("Average points:", average)

# Pack reward stars into boxes
stars_per_box = 10
boxes = total // stars_per_box
leftover_stars = total % stars_per_box

print("Complete reward boxes:", boxes)
print("Leftover stars:", leftover_stars)

# Compare with last week's points
last_week = 350
difference = total - last_week

print("\n===== WEEKLY COMPARISON =====")
print("Last week's points:", last_week)

if total > last_week:
    print("Points increased by", difference)
elif total < last_week:
    print("Points decreased by", abs(difference))
else:
    print("Points stayed the same")

# Update points using assignment operators
total += 20
print("\nAfter bonus points:", total)

total -= 10
print("After penalty points:", total)

total *= 2
print("After doubling points:", total)
