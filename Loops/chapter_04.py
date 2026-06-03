menu = ["Green", "Lemon", "Spiced", "Mint"]

# enumerate() function adds a counter to an iterable and returns it as an enumerate object.
#  The start parameter specifies the starting value of the counter. 
# In this case, we start counting from 1 instead of the default 0.
for idx, item in enumerate(menu, start=1):
    print(f"{idx}. {item} chai")