import os, random, string
os.system('cls')

ai_selection_upper_case = random.choice(string.ascii_uppercase)
print(ai_selection_upper_case)

ai_selection_lower_case = random.choice(string.ascii_lowercase)
print(ai_selection_lower_case)

ai_selection_punctuation = random.choice(string.punctuation)
print(ai_selection_punctuation)

ai_selection_numbers = random.randint(0,9)
print(ai_selection_numbers)

