import nltk
# print(nltk.help.upenn_tagset())

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.corpus import reuters

outdoor_colors = 'I walked up to the ice cream truck to place my order.'

outdoor_colors_words = word_tokenize(outdoor_colors)
outdoor_colors_tagged_words = pos_tag(outdoor_colors_words)

print(f"List of Words in 'outdoor_colors': {outdoor_colors_words}")
print(f"List of Tagged Words in 'outdoor_colors': {outdoor_colors_tagged_words}")