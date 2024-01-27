# o'zgaruvchi ?
w1 = input('So`z 1: ')
w2 = input('So`z 2: ')
a = len(w1)
b = len(w2)

if a > b:
    print(f'{w1}:{a} uzun {w2}:{b} dan.')
elif a == b:
    print(f'{w1}:{a} teng {w2}:{b} ga.')
else:
    print(f'{w1}:{a} kam {w2}:{b} dan.')
