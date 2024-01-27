import math
# 123 >= 3|234
a = math.sqrt(123)
b = math.pow(234, 1 / 3)
c = a >= b
print(f"{a:,.2f} >= {b:,.2f} -> {c}")
