# if else, elif
# a = float(input('Son: '))

# if 0 < a < 10 or 100 < a < 200 or 200 < a < 300:
#     pass
# elif -10 < a < 0:
#     pass
# elif a == 0:
#     pass
# else:
#     pass

# -----------------------
# if 0 < a < 10:
#     pass
#
# if -10 < a < 0:
#     pass
#
# if a == 0:
#     pass
# else:
#     pass


# ------------------------------
# hex, oct, int, bin
# 821298136126931
# b = int(input('son: '))
# hex_16 = hex(b)
# print(hex_16)
# son_10 = int(f'{hex_16}', 16)
# print(son_10)

# ------------------------------
# str
# a = int(input('son: '))  # 123
# b = str(a)  # '123'
# print(a, type(a))
# print(b, type(b))

# ------------------------------
# abs()  -absolut qiymat
# a = int(input('a: '))
# b = int(input('b: '))
# c = abs(a - b)
# print(c)

# ------------------------------
# random(), datetime, extend(), for,
# import random
#
# present = random.randint(1, 100)
# print(f'Sovrin egasi: {present}-raqam.')

# ------------------------------

# datetime
# import datetime
#
# now_ = datetime.datetime.now()
# print(now_)

# for loop
# ------------------------------
# for letter in 'Davron':
#     print(letter.upper(), end='_')


# a = {
#     'a': 0,
#     'b': 0,
# }
#
# letters = input('words: ')
# for letter in letters:
#     a[letter] += 1
# print(a)
# print(letters.count('a'))
# print(letters.count('b'))


# extend()

my_list = ['Alisher', 'Abbos', 'Davron']
print(my_list)
ism = input('ismingizni yozing: ')
my_list.extend([ism])
print(my_list)
