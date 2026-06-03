# Pure Function does not have any side effects and 
# always produces the same output for the same input.

def pure_chai(cups):
    return cups * 10


# Impure Function has side effects 
# and may produce different outputs for the same input.
# not recommended to use impure functions 
# as they can lead to unpredictable behavior and make debugging difficult.

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups


# Recursive Function is a function that calls itself in its definition.

def pour_chai(n):

    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)


print(pour_chai(3))


# Recursive Visualization diagram:

def pour_chai(n):

    print(n)

    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)


print(pour_chai(3))


# Lambda Function Example

chai_types = [
    "Light Chai",
    "Kadak Chai",
    "Ginger Chai",
    "Kadak Chai"
]
# Filter Example and lambda function to filter out "Kadak Chai" from the list of chai types.
strong_chai = list(
    filter(
        lambda chai: chai == "Kadak Chai",
        chai_types
    )
)

print(strong_chai)


# Reverse Filter Example

strong_chai = list(
    filter(
        lambda chai: chai != "Kadak Chai",
        chai_types
    )
)

print(strong_chai)