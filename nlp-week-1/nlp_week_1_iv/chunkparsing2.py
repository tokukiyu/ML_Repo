from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser


painting = "I finally told my mother my passion, which is that I love painting."
painting_words = word_tokenize(painting)
painting_tags = pos_tag(painting_words)

chunk_grammar_VP = "VP: {<VPD>*<VBG>}"
chunk_parser_VP = RegexpParser(chunk_grammar_VP)
print("\nChunked Verb Phrases in 'painting': \n", chunk_parser_VP.parse(painting_tags))