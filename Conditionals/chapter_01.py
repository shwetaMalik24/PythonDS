age = 20

if age >= 18:
    print("Adult")

#  if else example
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

# if elif else example
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# Logical operators example
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible")

logged_in = False

if not logged_in:
    print("Please login")

# Nested if example
age = 25
has_license = True

if age >= 18:

    if has_license:
        print("Can drive")

    else:
        print("License required")

else:
    print("Too young")

# Ternary operator example
age = 5

message = "Adult" if age >= 18 else "Minor"

print(message)

