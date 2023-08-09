from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from ner import coffee

# user defined ner 
def find_NEs(text):
  tokens = word_tokenize(text)
  tags = pos_tag(tokens)
  return(ne_chunk(tags))

print(f"\nName Entities in 'coffee' using User-Defined Function: {find_NEs(coffee)}")