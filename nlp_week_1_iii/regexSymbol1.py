import re
# this one is  the first file 
king = 'After the death of the king, everyone wanted to be a king.'
#
pattern1 = r'\sking'
match1 = re.findall(pattern1, king)
if match1:
    print(f'\nMatch! The pattern "{pattern1}" is in the sentence: "{king}"')
else:
    print(f'\nNo Match! The pattern "{pattern1}" is not in the sentence: "{king}"')
    
    