from fractions import Fraction

a = 1 / 2
b = 1 / 3
c = a + b
print(c)

# Fraction ichida ishaltiladgan sonlar faqat ``integer`` tipida bo'lishi kerak.
natija = Fraction(1, 2) + Fraction(1, 3)
print(natija)
