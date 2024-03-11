from decimal import Decimal

num = Decimal(input("number: "))

sqrtNum = Decimal("0")
# Keeps on incrementing the number until
# it reaches the square root
while sqrtNum != num/num:
  sqrtNum+=Decimal("0.00001")

print(f"sqrt of {num} is {sqrtNum}")
