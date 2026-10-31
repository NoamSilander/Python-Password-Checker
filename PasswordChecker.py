user_input = input('Enter a password: ')
points = 0

def check_length(psw):
    print(f'Length: {len(psw)} characters')
    if len(psw) >= 12:
        return True
    else:
        return False

def check_lower(psw):
    lower = False
    for char in psw:
        if char.islower():
            lower = True
    verdict = 'yes' if lower else 'no'
    print(f'Lowercase: {verdict}')
    return lower

def check_upper(psw):
    upper = False
    for char in psw:
        if char.isupper():
            upper = True
    verdict = 'yes' if upper else 'no'
    print(f'Uppercase: {verdict}')
    return upper

check_length(user_input)
check_lower(user_input)
check_upper(user_input)