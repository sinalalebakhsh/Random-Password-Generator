import os, random, string
from sys import flags
os.system('cls')

# ai_selection_upper_case = random.choice(string.ascii_uppercase)
# ai_selection_lower_case = random.choice(string.ascii_lowercase)
# ai_selection_punctuation = random.choice(string.punctuation)
# ai_selection_numbers = random.randint(0,9)

def choice_of_random_password(user_chice, numbers_characters):
    if user_chice == "random":
        list_1 = []
        flage = 0
        while flage != numbers_characters :
            for i in random.choice(string.printable):
                list_1.append(i)
                flage += 1
        print(f' this is random password:', ''.join(list_1))

def get_choice_user():
    user_choice = input('Do you want a random string or you want to customize?\nwrite "random" or "customize" : ----->')
    numbers_characters = int(input('What number of characters do you want?'))
    return user_choice, numbers_characters

def choice_of_customize_password(user_choice, numbers_characters):
    if user_choice == 'customize':
        list_1 = []
        flage = 0
        while flage != numbers_characters :
            get_select_uppercase = input('Do you want to have "Uppercase" letters? ')
            if get_select_uppercase == 'yes'.lower():
                ai_selection_upper_case = random.choice(string.ascii_uppercase)
                list_1.append(ai_selection_upper_case)
                flage += 1
            get_select_lowercase = input('Do you want to have "Lowercase" letters? ')
            if get_select_lowercase == 'yes'.lower():
                ai_selection_lower_case = random.choice(string.ascii_lowercase)
                list_1.append(ai_selection_lower_case)
                flage += 1
               
        print(f'this is customize password:', ''.join(list_1))
            


user_choice, numbers_characters = get_choice_user()

choice_of_random_password(user_choice, numbers_characters)

choice_of_customize_password(user_choice, numbers_characters)

