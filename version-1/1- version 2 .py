import os, random, string
os.system('cls')

# ai_selection_upper_case = random.choice(string.ascii_uppercase)
# print(ai_selection_upper_case)

# ai_selection_lower_case = random.choice(string.ascii_lowercase)
# print(ai_selection_lower_case)

# ai_selection_punctuation = random.choice(string.punctuation)
# print(ai_selection_punctuation)

# ai_selection_numbers = random.randint(0,9)
# print(ai_selection_numbers)

# ai_all_letters_punc_numb1 =  random.choice(string.printable)
# print(ai_all_letters_punc_numb1, end='')

# ai_all_letters_punc_numb2 =  random.choice(string.printable)
# print(ai_all_letters_punc_numb2, end='')

# ai_all_letters_punc_numb3 =  random.choice(string.printable)
# print(ai_all_letters_punc_numb3, end='')

# ai_all_letters_punc_numb4 =  random.choice(string.printable)
# print(ai_all_letters_punc_numb4, end='')

list_1 = []
flage = 0
while flage != 5 :
    for i in random.choice(string.printable):
        list_1.append(i)
        flage += 1

print(f' this is random password:', ''.join(list_1))