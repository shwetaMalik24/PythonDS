def make_chai():
    return "Here is your masala chai"

return_value = make_chai()

print(return_value)

def make_chai():
    print("Here is your masala chai")

return_value = make_chai()

print(return_value) 

def chaiwala():
    pass

print(chaiwala())



def sold_cups():
    return 120

total = sold_cups()

print(total)

def chai_status(cups_left):

    if cups_left == 0:
        return "Sorry, Chai Over"

    return "Chai Ready"

print(chai_status(0))
print(chai_status(5)) 



def chai_report():
    return 120, 80

sold, remaining = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)

def chai_report():
    return 120, 80, 10

sold, remaining, _ = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)