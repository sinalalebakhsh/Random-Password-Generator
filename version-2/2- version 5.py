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

def get_length_of_password(option, default, pass_max_length=35, pass_min_length=5):
    while True:
        user_password_length = input(f'Enter password length. default= {default}. Write numbers or Press Enter: ')
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
            user_password_length = get_length_of_password(option, default)

get_setting_from_user(settings)
print(settings)











