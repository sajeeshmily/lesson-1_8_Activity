
# Smart School Day Planner

weather = input("What is the weather? (sunny/rainy/cloudy): ").lower()
homework = input("Is your homework done? (yes/no): ").lower()
holiday = input("Is today a holiday? (yes/no): ").lower()

print("\n===== SMART SCHOOL DAY PLAN =====")

# Classify the day
if holiday == "yes":
    print("Today is a holiday!")

elif weather == "sunny" and homework == "yes":
    print("It is sunny and homework is done.")
    print("Plan: Go outside and enjoy your day!")

elif weather == "rainy" or weather == "cloudy":
    print("The weather is rainy or cloudy.")
    print("Plan: Stay indoors and read a book.")

elif not (homework == "yes"):
    print("Your homework is not done.")
    print("Plan: Finish your homework first.")

else:
    print("Plan: Attend school, study, and enjoy your day!")

# Combine AND, OR, and NOT
if (weather == "sunny" and homework == "yes") or not (homework == "yes"):
    print("Special plan: Choose an activity based on your homework status.")

print("\nHave a wonderful day!")
