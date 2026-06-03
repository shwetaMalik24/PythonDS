# Built-in functions are functions that are provided by Python 
# and are always available for use. 
# They are defined in the Python standard library 
# and can be used without importing any additional modules.
def chai_flavor(flavor="Masala"):
    """
    Returns the flavor of chai.
    """
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)
help(len)



def generate_bill(chai=0, samosa=0):
    """
    Calculates total bill for chai and samosa.

    Param chai:
        Number of chai cups.
        10 rupees each.

    Param samosa:
        Number of samosas.
        15 rupees each.

    Returns:
        Total amount and thank you message.
    """
    print(generate_bill.__doc__)
    print(generate_bill.__name__)

    total = (chai * 10) + (samosa * 15)
    return total, "Thank you for visiting chaicode.com"