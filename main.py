import random
import string
def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special

    pwd = ''
    meet_criteria = False
    has_number = False
    has_specail = False
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd +=new_char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_specail = True
        meets_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_specail
    return pwd
min_length = int(input('Minimal uzunlikni kiriting:'))
has_number = input('Raqamlarga ega bolishni xohlaysizmi (ha/yoq)').lower()=='ha'
has_spechial = input('Maxsus belgilarga ega bo\'lishni xohlaysizmi (ha/yoq)?').lower()=='ha'


pwd = generate_password(10)
print(f"Yaratilgan parol ->  {pwd}")