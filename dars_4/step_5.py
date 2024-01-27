from dars_4.step_4 import admin, admin_parol

login = input('Login: ')
password = int(input('Password: '))

if admin == login and password == admin_parol:
    print('Shaxsiy akkountga xush kelibsiz!')
else:
    print('Login yoki parol xato!')
