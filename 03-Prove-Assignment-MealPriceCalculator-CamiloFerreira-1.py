childMealPrice = float(input ("What is the price of a child's meal? "))
adultMealPrice = float(input ("What is the price of a adult's meal? "))
childrenQty = int(input ("How many children are there? "))
adultQty = int(input ("How many adults are there? "))
taxRate = float(input ("What is the sales tax rate? "))
subtotal = childMealPrice * childrenQty + adultMealPrice * adultQty
salesTax = subtotal * taxRate / 100
total = subtotal + salesTax

print("\nSubtotal: $"+str(subtotal))
print("Sales Tax: $"+str(salesTax))
print("Total: $"+str(total))

paymentAmount = float(input ("\nWhat is the payment amount? "))
changeAmount = round(paymentAmount - total,2)
print("Change: $" + str(changeAmount))