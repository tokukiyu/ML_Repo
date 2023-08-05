from nltk.tokenize import RegexpTokenizer



uppercase_pattern = RegexpTokenizer('[A-Z]+', gaps = False)
magic = 'My teacher, Ms. Sanford, said there Is always magic in the air if you believe in it.'
magic_tokenized = uppercase_pattern.tokenize(magic)
print(f"\nRegexp Tokenizer by Uppercase Tokenized Output of 'magic': {magic_tokenized}")

# hello update