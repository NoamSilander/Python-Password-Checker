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

def check_digit(psw):
    digit  = False
    for char in psw:
        if char.isdigit():
            digit = True
    verdict = 'yes' if digit else 'no'
    print(f'Number: {verdict}')
    return digit

def check_symbol(psw):
    symbol  = False
    for char in psw:
        if not char.isalnum():
            symbol = True
    verdict = 'yes' if symbol else 'no'
    print(f'Symbol: {verdict}')
    return symbol

def check_strength(psw):
    points = 0
    strength = ''
    needed_list= []
    if check_length(psw):
        points += 1
    else:
        needed_list.append('Make it atleast 12 characters')
    if check_lower(psw):
        points += 1
    else:
        needed_list.append('Add lowercase letters')
    if check_upper(psw):
        points += 1
    else:
        needed_list.append('Add uppercase letters')
    if check_digit(psw):
        points += 1
    else:
        needed_list.append('Add numbers')
    if check_symbol(psw):
        points += 1
    else:
        needed_list.append('Add symbols')
    if points == 1:
        strength = 'Very weak'
    elif points == 2:
        strength = 'Weak'
    elif points == 3:
        strength = 'Average'
    elif points == 4:
        strength = 'Strong'
    elif points == 5:
        strength = 'Very strong (good job)'
    print(f'Strength: {strength}')
    if not needed_list:
        needed_list.append('None')
    print(f'To improve: {', '.join(needed_list)}')

while True:
    user_input = input('Enter a password (enter to exit): ')
    if user_input == '':
        break
    check_strength(user_input)

