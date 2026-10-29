
# Daily Activity Planner

homework = int(input("How many hours of homework do you have? "))
free_time = int(input("How many hours of free time do you have? "))

print("\n===== YOUR DAILY PLAN =====")

if homework > 2:
    print("Start homework early and take short breaks.")
else:
    print("Finish your homework before playing.")

if free_time >= 2:
    print("You have time for games, hobbies, or sports!")
else:
    print("Use your free time wisely and relax.")

if homework > free_time:
    print("Give priority to your homework today.")
else:
    print("Balance homework with your favourite activities.")

print("\nHave a productive day!")
