from nltk import Index

pos_tags = {'education': 'N', 'neat': 'ADJ', 'extend': 'V', 'sweet': 'ADJ', 'deflation': 'N', 'bend': 'V'}
pos_tags3 = Index((value,key) for (key,value) in pos_tags.items())
print("\nOriginal pos_tags dictionary combined with new pos_tags3 dictionary:", pos_tags3)
print("All words in pos_tags_3 that are identified as 'V':", pos_tags3['V'])