import opcode
import os
os.system('cls')

settings = {
    'lower' : True,
    'upper' : True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
}

def get_length_of_password(option, default):
    while True:
        user_password_lenght = input(f'Enter password length. default= {default}. Write numbers or Press Enter: ')
        if user_password_lenght == '':
            return default
        if user_password_lenght.isdigit() and int(user_password_lenght) > 2 :
            settings[option] = int(user_password_lenght)
            return settings[option]

        print('*** Write Just from numbers. ***')

def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (default: {default}) (y: yes, n: no, Press Enter for default): ')
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
            user_password_lenght = get_length_of_password(option, default)

get_setting_from_user(settings)

print(settings)











