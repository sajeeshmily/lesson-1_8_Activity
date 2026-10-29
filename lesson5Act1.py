
# Weather Outfit Picker

temperature = int(input("Enter temperature in Celsius: "))
rain = input("Is it raining? (yes/no): ").lower()
wind = input("Is it windy? (yes/no): ").lower()
puddles = input("Are there puddles? (yes/no): ").lower()

print("\n===== YOUR WEATHER OUTFIT =====")

# Choose clothes
if temperature < 15:
    print("Wear a warm jacket!")
else:
    print("Wear a light shirt!")

# Choose umbrella
if rain == "yes":
    print("Carry an umbrella!")
else:
    print("No umbrella needed.")

# Choose windbreaker
if wind == "yes":
    print("Wear a windbreaker!")
else:
    print("No windbreaker needed.")

# Choose shoes
if puddles == "yes":
    print("Wear waterproof shoes!")
else:
    print("Regular shoes are fine.")

print("\nHave a great day!")
