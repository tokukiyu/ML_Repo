import re

king = 'After the death of the king, everyone wanted to be a king.'

pattern2 = r'k..g$'
match2 = re.findall(pattern2, king)
if match2:
    print(f'\nMatch! The pattern {pattern2} is in the sentence:{king}')
else:
    print(f'\nNo Match! The pattern {pattern2} is not in the sentence: {king}')