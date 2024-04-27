"""
Objective:
Create a Python tool that checks the strength of a password based on various criteria.

**Requirements:
1. Length Check: The password must be at least 12 characters long.
2. Character Diversity: The password should include uppercase letters, lowercase letters, numbers, and at least two special characters (e.g., !, @, #, $).
3. Common Password Check: The tool should compare the password against a list of the 1000 most common passwords and flag if the password is too common. You will need to create or find a list of common passwords to use for this check.

Output:
- Provide a detailed report on which criteria the password met and which it did not.
- Overall strength rating (e.g., Weak, Moderate, Strong) based on the number of criteria met.

This project will help you practice handling strings, using regular expressions, reading from files, and applying logical checks—skills that are very useful in many areas of software development, including cybersecurity.
"""

import string
import re

min_length: int = 12


def check_password(pwd: str):
    def check_length():
        "1. Length Check: The password must be at least 12 characters long."

        return len(pwd) >= min_length

    def check_character_diversity():
        "2. Character Diversity: The password should include uppercase letters, lowercase letters, numbers, and at least two special characters (e.g., !, @, #, $)."

        has_upper = re.search(r"[A-Z]", pwd) is not None
        has_lower = re.search(r'[a-z]', pwd) is not None
        has_digit = re.search(r'[0-9]]', pwd) is not None
        has_special_chars = len(re.findall(rf'[{string.punctuation}]', pwd)) >= 2

        return (has_upper, has_lower, has_digit, has_special_chars)

    def check_common_pwd():
        "3. Common Password Check: The tool should compare the password against a list of the 1000 most common passwords and flag if the password is too common. You will need to create or find a list of common passwords to use for this check."

        def load_common_pwd_list():
            with open('10-million-password-list-top-10000.txt', 'rt') as f:
                common_pwd_list: list = [line.strip() for line in f.readlines()]
                return common_pwd_list

        for common_word in load_common_pwd_list():
            if common_word in pwd:
                return (False, common_word)
            else:
                return True

    is_long = check_length()
    has_upper, has_lower, has_digit, has_special_chars = check_character_diversity()
    is_diverse = (has_upper, has_lower, has_digit, has_special_chars).count(True) >= 3
    is_unique = check_common_pwd()

    def strength_rating():
        _ = (is_long, has_upper, has_lower, has_digit, has_special_chars, is_unique)
        counting_true = _.count(True)
        if counting_true >= 5:
            return 'Strong'
        elif counting_true >= 3:
            return 'Moderate'
        else:
            return 'Weak'

    print(f"""Long Enough: {is_long};\nCharacter Diversity: {is_diverse};\nUnique: {is_unique}""")
    print(f'Security Level: {strength_rating()}')


password = str(input('Please input your password here: '))
check_password(password)
