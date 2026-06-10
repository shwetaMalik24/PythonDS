# def serve_chai():
#     yield "Masala Chai"
#     yield "Ginger Chai"
#     yield "Elaichi Chai"

# stall = serve_chai()
# print(stall)  # This will print the generator object

# for cup in stall:
#     print(cup)

def get_chai_gen():
    yield "Cup One"
    yield "Cup Two"
    yield "Cup Three"

chai = get_chai_gen()

# next give me first result of generator.
# multiple next will give you next result of generator.
# for the first time it will give you "Cup One", 
# second time "Cup Two" and third time "Cup Three"
print(next(chai))
print(next(chai))
print(next(chai))
# fourth time it will give you StopIteration error because there is no more value to yield.
print(next(chai))