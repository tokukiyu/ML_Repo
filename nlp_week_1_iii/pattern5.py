import re
from pattern4 import numbers

pattern7 = r'(\d+-\d+-\d+)'
pattern8 = r'(\d+)-\d+-\d+'
patterns78 = [pattern7, pattern8]
for pattern in patterns78:
    if re.findall(pattern, numbers):
        print(f'\nMatch! At least one of the numbers in {pattern} is in the string: {numbers}')
        print(f'Pattern found: {re.findall(pattern, numbers)}')
    else:
     print(f'\nNo Match! None of the numbers in {pattern} are in the string: {numbers}')