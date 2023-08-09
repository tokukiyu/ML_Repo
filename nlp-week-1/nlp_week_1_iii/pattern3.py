import re

dessert = 'The most awesome meal of the day is dessert because it can be whatever you want.'

pattern3 = r'de.*ert'
match3 = re.findall(pattern3, dessert)
if match3:
    print(f'\nMatch! The pattern "{pattern3}" is in the sentence: "{dessert}"')
else:
    print(f'\nNo Match! The pattern "{pattern3}" is not in the sentence: "{dessert}"')
    
    