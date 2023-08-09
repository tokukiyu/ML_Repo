from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser


head_quote = "It's strange how a word, a phrase, a sentence, can feel like a blow to the head."
head_quote_words = word_tokenize(head_quote)
head_quote_tags = pos_tag(head_quote_words)

chunk_grammar_NP_noVB = """
  NP: {<DT><NN.*><.*>*<NN.*>}
  }<VB.*>{"""

chunk_parser_NP_noVB = RegexpParser(chunk_grammar_NP_noVB)
head_quote_chunked2 = chunk_parser_NP_noVB.parse(head_quote_tags)
print("\nChunked Noun Phrases in 'head_quote' without Verbs: \n", head_quote_chunked2)