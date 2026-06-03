chai = "Ginger Chai"

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai)

print(chai)

chai = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)

print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai(
    "Darjeeling",
    "Yes",
    "Low"
)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai(
    tea="Green",
    sugar="Medium",
    milk="No"
)

def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)

special_chai(
    "Cinnamon",
    "Cardamom",
    sweetener="Honey",
    foam="Yes"
)

# default parameters
def chai_order(order=[]):
    order.append("Masala Chai")
    print(order)

chai_order()
chai_order()


def chai_order(order=None):

    if order is None:
        order = []

    print(order)

chai_order()
chai_order("Lemon Chai")