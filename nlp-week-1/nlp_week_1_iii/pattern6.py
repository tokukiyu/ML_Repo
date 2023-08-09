import re
numbers2 = '14590813302'
pattern10 = r'(1|2|3)\d{3}'
pattern9 = r'[1-3]\d{3}'
patterns910 = [pattern9, pattern10]
for pattern in patterns910:
    if re.findall(pattern, numbers2):
        print(f'\nMatch! At least one of the numbers in \
        {pattern} is in the string: {numbers2}')
        print(f'Pattern found: {re.findall(pattern, numbers2)}')
    else:
        print(f'\nNo Match! hell no, None of the numbers in {pattern} are \
        in the string: {numbers2}')
        