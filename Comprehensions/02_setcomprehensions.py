
numbers = {1,2,2,2,4,5,4,5,6,7,8,9}
square = {x*2 for x in numbers if x%2!=0}
print(square)

recipes = {
    "Masala Chai": [
        "Ginger",
        "Cardamom",
        "Clove"
    ],

    "Elaichi Chai": [
        "Cardamom",
        "Milk"
    ],

    "Spicy Chai": [
        "Ginger",
        "Black Pepper",
        "Clove"
    ]
}

unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

print(unique_spices)