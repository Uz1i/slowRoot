from decimal import Decimal

num = Decimal(input("number: "))

sqrtNum = Decimal("0")

while sqrtNum != num/num:
  sqrtNum+=Decimal("0.00001")

print(f"sqrt of {num} is {sqrtNum}")
