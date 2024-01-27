admin = 'Asadbek'
admin_parol = 1234
if __name__ == '__main__':
    login = input('Login: ')
    password = int(input('Password: '))

    if admin == login:
        if password == admin_parol:
            print('Shaxsiy akkountga xush kelibsiz!')
        else:
            print('Parol xato!')
    else:
        print('Login xato!')





