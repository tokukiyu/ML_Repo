from nltk.tokenize import word_tokenize
from nltk import pos_tag

near_beach = "Near the beach, there are tennis and basketball courts, parks and playgrounds."
near_beach_tokens = word_tokenize(near_beach)
near_beach_nouns = [token for (token, token_pos_tag) in pos_tag(near_beach_tokens) if token_pos_tag == 'NN']

print("Nouns in 'near_beach': ", near_beach_nouns)
