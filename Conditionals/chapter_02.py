
# Conditionals are used to make decisions in code. They allow us to execute certain blocks of code based on specific conditions. In this example, we will ask the user for their preferred snack and serve them accordingly.
# input() function is used to take input from the user. The .lower() method is used to convert the input to lowercase, making the comparison case-insensitive.
snack = input("Enter your preferred snack ").lower()

print(f"User said {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")


cup = input("Enter your preferred cup size ").lower()

if cup == "small":
    print("10")
elif cup == "medium":
    print("15")
elif cup == "large":
    print("20")
else:
    print("Unknown")