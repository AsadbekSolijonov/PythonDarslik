# Savol: Quyidagi ro'yxatdan 7 ga bo'lianadigan sonlarni
# olib boshqa yangi ro'yxatga qo'shib beruvchi dastur tuzing.
numbers = [180, 847, 32, 56, 40, -45, 96, 63, 35, 70, 107, 105]
numbers_7 = []
for son in numbers:
    if son % 7 == 0:
        numbers_7.append(son)

for son_7 in numbers_7:
    numbers.remove(son_7)

print(f"numbers: {numbers}")
print(f"numbers_7: {numbers_7}")
