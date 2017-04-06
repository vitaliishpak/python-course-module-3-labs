##Laboratory Work 3.5

####Description:

Write a program that will take username and password, checks if they are in registered users dictionary, if they are present – print “Access Granted”, if not – handle it using KeyError Eception handling. Raise RuntimeError and handle it if the name is empty. For registered user, which is logged - let him know if their password has unacceptable symbols (non alphanumeric) and propose to change it using a dialog.

####Here is its solution code:

*solution_3_5.py*
```python
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
```