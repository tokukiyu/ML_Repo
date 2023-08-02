import re
from re import finditer

adv_sentence = "After last summer's adventures, we're up to any task!"

pattern2 = ['adventures', 'adventure', 'dog']
for element in pattern2:
    if re.search(element, adv_sentence):
        print(f'\nMatch! The computer found the pattern "{element}" in the sentence: "{adv_sentence}"')
    else:
        print(f'\nNo Match! The computer was not able to find the pattern "{element}" in the sentence: "{adv_sentence}"')
