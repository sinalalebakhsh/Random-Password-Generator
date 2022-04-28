import os, random
import string
from symtable import Symbol
os.system('cls')
settings = {
    'upper' : True,
    'lower' : True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
}
def get_length_of_password(option, default, pass_max_length=35, pass_min_length=5):
    while True:
        user_password_length = input('Enter password length.'
                                     f' default= {default}.'
                                     ' Write numbers or Press Enter: ')
        if user_password_length == '':
            return default
        if user_password_length.isdigit():
            integer_user_pass_length = int(user_password_length)
            if pass_max_length > integer_user_pass_length > pass_min_length :
                settings[option] = integer_user_pass_length
                return settings[option]
            elif integer_user_pass_length >= pass_max_length:
                print(f'Maximom length {pass_max_length} !!')
            elif 0 <= integer_user_pass_length <= pass_min_length:
                print(f'Mimimom length {pass_min_length} !!')
        print('*** Try again ***')
        if not user_password_length.isdigit():
            print('Write Just from numbers.')
def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}?'
                           f' (default: {default})'
                            ' (y: yes, n: no, Press Enter for default): ')
        if user_input == '':
            return default
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('**** Invalide input. Please try again ****')
def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
                user_choice = get_yes_or_no_for_settings(option, default)
                settings[option] = user_choice
        else:
            user_password_length = get_length_of_password(option, default)       
def selection_uppercase_letter():
    return random.choice(string.ascii_uppercase)
def selection_lowercase_letter():
    return random.choice(string.ascii_lowercase)
def selection_symbols():
    return random.choice("""'!@#$%^&*()_+?><":'\\/.][}{-~""")
def generate_random_char(choices):
    choice_org = random.choice(choices)
    if choice_org == 'upper':
        return selection_uppercase_letter()
    if choice_org == 'lower':
        return selection_lowercase_letter()
    if choice_org == 'symbol':
        return selection_symbols()
    if choice_org == 'number':
        return random.choice('0123456789')
    if choice_org == 'space':
        return ' '
def password_generator(settings):
    password_org = ''
    password_length = settings['length']
    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'number', 'space']))

    for number in range(password_length):
        password_org += generate_random_char(choices)
    return password_org

get_setting_from_user(settings)
print()
print(password_generator(settings), '\n')

