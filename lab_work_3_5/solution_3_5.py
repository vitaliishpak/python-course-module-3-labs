registered_users = {
    'Vitalii': 'a123456*',
    'Oleh': '987654',
    'Ivan': 'qwerty',
    'Andrii': 'Andrii'
}

try:
    username = input('Please, enter you username:')
    password = input('Please, enter you username:')

    if username == '':
        raise RuntimeError

    if registered_users[username] == password:
        print('Access Granted!')
        if not password.isalnum():
            while True:
                print('You password is not alphanumeric!')
                new_password = input('Please, enter correct new password value:')
                if new_password.isalnum():
                    registered_users[username] = new_password
                    print('Your new password successfully saved!')
                    break
    else:
        raise Exception

except RuntimeError:
    print('Empty username passed!')

except KeyError:
    print('There is no user with such username!')

except Exception:
    print('Incorrect password!')
