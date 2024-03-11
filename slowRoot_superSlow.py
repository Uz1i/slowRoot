from decimal import Decimal
from random import choice

# Create a list of numbers
list = []
listNum = Decimal("0")
for i in range(10000000):
  list.append(listNum+=Decimal("0.00001"))

squareNumber = Decimal(input("Number: "))
  
# Randomly choose a number from the list until it is the square root of the number

sqrtNum = Decimal("0")
while sqrtNum**2 != squareNumber:
  sqrtNum == choice(list)

print(f"sqrt of {squareNumber} is {sqrtNum}")
