def infinitechai():
    count = 1

    while True:
        yield f"Refill {count}"
        count += 1


refill = infinitechai()

for _ in range(3):
    print(next(refill))


def infinitechai():
    count = 1

    while True:
        yield f"Refill {count}"
        count += 1


refill = infinitechai()

for _ in range(5):
    print(next(refill))


user2 = infinitechai()

for _ in range(6):
    print(next(user2))