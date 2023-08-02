import re
from re import finditer

adv_sentence = "After last summer's adventures, we're up to any task!"

pattern = r'...adventure'

match = re.search(pattern, adv_sentence)
if match != None:
    print(
        f"\nThere is a match. The string 'adventure' starts on the {match.start()}th letter.")
else:
    print("\nThe computer wasn't able to find a match.")

