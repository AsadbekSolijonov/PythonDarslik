start = int(input('start: '))
end = int(input('end: '))
toq_son = []
juft_son = []

for son in range(start, end + 1):
    if son % 2 == 0:
        juft_son.append(son)
    elif son % 2 != 0:
        toq_son.append(son)

print(f'Juft son: {juft_son}')
print(f'Toq son: {toq_son}')


# Uyga vazifa:
# 2 va 5
# 3 va 4
# 7 va 5
# 6 va 7
# 9 va 2
# ga bo'linadiganlarini alohida listga joylovchi algoritim yozing.
