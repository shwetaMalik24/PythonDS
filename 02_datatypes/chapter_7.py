# Mutable List Example

ingredients = ["water", "milk", "black tea"]

# Add sugar
ingredients.append("sugar")

print("Ingredients are:", ingredients)

# Remove water
ingredients.remove("water")

print(ingredients)


# Another example

spice_options = ["ginger", "cardamom"]

chai_ingredients = ["water", "milk"]

# Combine lists
chai_ingredients.extend(spice_options)

print("chai", chai_ingredients)


# Insert at specific position
chai_ingredients.insert(2, "black tea")

print(chai_ingredients)


# Pop last element
last_added = chai_ingredients.pop()

print(last_added)

print(chai_ingredients)


# Reverse list
chai_ingredients.reverse()

print(chai_ingredients)


# Sort list
chai_ingredients.sort()

print(chai_ingredients)


# Max and Min example

sugar_levels = [1, 2, 3, 4, 5]

print("Maximum sugar level:", max(sugar_levels))

print("Minimum sugar level:", min(sugar_levels))