
import keyword

name = input("What is your name? ")
goal = input("What is your personal goal? ")
time = input("When do you want to achieve it? ")

print("\n===== MY PERSONAL GOAL PLAN =====")

print("Name:", name)
print("My Goal:", goal)
print("Target Time:", time)

print("\nKeep working towards your goal, ", end="")
print(name, end="!")

print("\n\nPython keywords are:")
print(keyword.kwlist)
