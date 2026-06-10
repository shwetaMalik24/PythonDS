# [expressions, for items in Iterable, if condition]

square = [x**2 for x in range(10) if x%2==0]
print(square)

teas = [
    "Masala",
    "Green",
    "Black",
    "Iced"
]

hot_teas = [
    tea
    for tea in teas
    #  if tea != "Iced"
    if "Iced" not in tea
]

print(hot_teas)