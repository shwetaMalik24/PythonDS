def calculateBill(cups, pricePerCup):
    return cups * pricePerCup

myBill = calculateBill(3, 15)

print(myBill)

print(
    "Order for table 2:",
    calculateBill(2, 50)
)


def addVAT(price, vatRate):
    return price * ((100 + vatRate) / 100)

orders = [100, 150, 200]

for price in orders:
    finalAmount = addVAT(price, 10)

    print(
        f"Original: {price}, "
        f"Final with VAT: {finalAmount}"
    )