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

def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (default is {default}) (y: yes, n: no): ')
        if user_input == '':
            return default
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('**** Invalide input. Please try again ****')

def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
                get_yes_or_no_for_settings(option, default)



get_setting_from_user(settings)

print(settings)











