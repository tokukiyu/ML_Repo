from nltk.tokenize import RegexpTokenizer

white_space_pattern = RegexpTokenizer('\s+', gaps = True)
#  ####
codio = 'Codio is the best computer science? learning tool.'
codio_tokenized = white_space_pattern.tokenize(codio)
print(f"\nOriginal Output of 'codio': {codio}")
print(f"\nRegexp Tokenizer Tokenized Output of 'codio': {codio_tokenized}")