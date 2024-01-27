a = int(input('A sonni kiriting:'))
b = int(input('B sonni kiriting:'))
c = int(input('C sonni kiriting:'))

count_plus = 0
count_no_pm = 0
count_minus = 0

if a > 0:
    count_plus += 1
elif a < 0:
    count_minus += 1
elif a == 0:
    count_no_pm += 1

if b > 0:
    count_plus += 1
elif b < 0:
    count_minus += 1
elif b == 0:
    count_no_pm += 1

if c > 0:
    count_plus += 1
elif c < 0:
    count_minus += 1
elif c == 0:
    count_no_pm += 1

print(f"Musbat son: {count_plus} ta")
print(F"Manfiy son: {count_minus} ta")
print(f"Nol soni: {count_no_pm} ta")
