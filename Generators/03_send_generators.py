def chai_customer():
    print("Welcome!")
    print("What chai would you like?")
    # taking first order from the customer
    order = yield

    while True:
        print(f"Preparing {order}")
        # taking next order from the customer
        # if comment the below line then it will not take next order 
        # and will keep preparing the first order only.
        order = yield


stall = chai_customer()

# start the generator
next(stall)

# send the order to the generator
stall.send("Masala Chai")

stall.send("Lemon Chai")