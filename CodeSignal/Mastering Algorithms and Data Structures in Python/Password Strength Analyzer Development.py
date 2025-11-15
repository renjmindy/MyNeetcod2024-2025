def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    special_characters_list = list(special_characters)

    # implement this
    #pass
    ans = list()
    
    is_at_least_eight, is_digit, is_upper, is_lower, is_special = False, False, False, False, False
    
    for password in passwords:
        is_at_least_eight, is_digit, is_upper, is_lower, is_special = False, False, False, False, False
        if len(password) >= 8: is_at_least_eight = True
        for c in password:
            if c.isdigit(): is_digit = True
            if c.isupper(): is_upper = True
            if c.islower(): is_lower = True
            if c in special_characters_list: is_special = True
            
        ans.append(
            {
                'length': is_at_least_eight,
                'digit': is_digit,
                'lowercase': is_lower,
                'uppercase': is_upper,
                'special_char': is_special
            }
        )

    return ans

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
