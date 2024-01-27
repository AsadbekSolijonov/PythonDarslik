import math

print(f"""[0] - Doira
[1] - Kub
[2] - Paralelopiped
[3] - Uchburchak
[4] - To'g'ri to'rtburchak""")

tanla = int(input("Tanla: "))

if tanla == 0:
    print('Doira ichidasiz!')
    R = float(input('Radius: '))
    pi = 3.14
    L = 2 * pi * R
    S = pi * R ** 2
    print(f'Doiraning uzunligi: {L} m')
    print(f'Doiraning yuzasi: {S} m2')
elif tanla == 3:
    print('Uchburchak ichidasiz!')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    P = a + b + c
    p = P / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'Uchburchakning perimetri: {P} m')
    print(f'Uchburchakning yuzasi: {S} m2')
elif tanla == 4:
    print('To`rtburchak ichidasiz!')
    a = float(input('a: '))
    b = float(input('b: '))
    P = 2 * (a + b)
    S = a * b
    print(f'To`rtburchakni perimetri: {P} m')
    print(f'To`rtburchakni yuzasi: {S} m2')
elif tanla == 1:
    print('Kub ichidasiz:')
    a = float(input('a: '))
    V = a ** 3
    print(f"Kubning xajmi: {V} m3")

elif tanla == 2:
    print('Paralelopiped ichidasiz:')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    V = a * b * c
    print(f"Paralelopiped hajmi: {V} m3")
else:
    print('Tanlovda adashdingiz!\nIltimos qayta harakat qilib ko`ring!')
