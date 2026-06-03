# In this example, we have two lists: names and bills. 
# We want to print out how much each person paid. 
# The zip() function is used to combine the two lists into pairs of corresponding elements. 
# The for loop then iterates over these pairs, allowing us to access both the name and the amount paid in each iteration. 
# The f-string is used to format the output in a readable way.
names = ["Hitesh", "Meera", "Sam", "Ali"]

bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")