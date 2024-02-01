start = int(input('start: '))
end = int(input('end: '))

list_2_5 = []
list_3_4 = []
list_7_5 = []
list_6_7 = []
list_9_2 = []

for son in range(start, end + 1):
    if son % 2 == 0 and son % 5 == 0:
        list_2_5.append(son)

    if son % 3 == 0 and son % 4 == 0:
        list_3_4.append(son)

    if son % 7 == 0 and son % 5 == 0:
        list_7_5.append(son)

    if son % 6 == 0 and son % 7 == 0:
        list_6_7.append(son)

    if son % 9 == 0 and son % 2 == 0:
        list_9_2.append(son)

print(f" list_2_5: {list_2_5}")
print(f" list_3_4: {list_3_4}")
print(f" list_7_5: {list_7_5}")
print(f" list_6_7: {list_6_7}")
print(f" list_9_2: {list_9_2}")

# Uyga vazifa:
# 2 va 5
# 3 va 4
# 7 va 5
# 6 va 7
# 9 va 2
