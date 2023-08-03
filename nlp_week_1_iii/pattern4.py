import re
numbers = '315-897-4873'
pattern4 = r'[123]'
pattern5 = r'[1-3]'
pattern6 = r'[^1-5]'
patterns456 = [pattern4, pattern5, pattern6]
for pattern in patterns456:
    if re.findall(pattern, numbers):
     print(f'\nMatch! At least one of the numbers in {pattern} is in the string: {numbers}')
    else:
        print(f'\nNo Match! None of  the numbers in {pattern} are in the string: {numbers}')
        