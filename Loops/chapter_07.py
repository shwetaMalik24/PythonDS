flavors = [
    "ginger",
    "out of stock",
    "lemon",
    "discontinued",
    "tulsi"
]

for flavor in flavors:

    if flavor == "out of stock":
        continue

    if flavor == "discontinued":
        print("Discontinued item found")
        break

    print(f"{flavor} item found")

print("Outside of loop")



staff = [
    ("Amit", 16),
    ("Zara", 17),
    ("Raj", 15)
]

for name, age in staff:

    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break

else:
    print("No one is eligible to manage the staff")