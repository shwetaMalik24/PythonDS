# Tuples in Python

# Creating a tuple
masala_spices = (
    "cardamom",
    "clove",
    "cinnamon"
)

# Tuple unpacking
spice_one, spice_two, spice_three = masala_spices

print(
    f"Main masala spices are "
    f"{spice_one}, {spice_two}, {spice_three}"
)

# Tuple packing / multiple variable assignment
ginger_ratio, cardamom_ratio = 2, 1

print(
    f"Ratio is G:{ginger_ratio} "
    f"and C:{cardamom_ratio}"
)

# Swapping variables using tuples
ginger_ratio, cardamom_ratio = (
    cardamom_ratio,
    ginger_ratio
)

print(
    f"After swapping -> "
    f"G:{ginger_ratio} "
    f"and C:{cardamom_ratio}"
)

# Membership testing
print(
    "ginger" in masala_spices
)

print(
    "cinnamon" in masala_spices
)

# Case-sensitive membership testing
print(
    "Cinnamon" in masala_spices
)