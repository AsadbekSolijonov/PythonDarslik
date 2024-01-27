from decimal import Decimal

error = 0.1 + 0.2  # 0.30000000000000004
print(error)
true = Decimal('0.1') + Decimal('0.2')  # 0.3
print(true)

