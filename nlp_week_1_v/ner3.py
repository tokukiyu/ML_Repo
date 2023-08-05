from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

def find_NEs_pretty2(text):
  tokens = word_tokenize(text)
  tags = pos_tag(tokens)
  NEs = ne_chunk(tags, binary=True)
  entities = []
  for chunked_word in NEs:
    if hasattr(chunked_word, 'label') and chunked_word.label() == 'NE':
      named_entity = ' '.join(word[0] for word in chunked_word)
      entities.append(named_entity)
  return entities

space = 'John try to replicate the magic of Star Trek, but none have succeeded.'

print(f"\nName Entities in 'space' using hasattr(): {find_NEs_pretty2(space)}")



def find_NEs_pretty2(text):
  tokens = word_tokenize(text)
  tags = pos_tag(tokens)
  NEs = ne_chunk(tags)
  entities = []
  for chunked_word in NEs:
    if hasattr(chunked_word, 'label') and chunked_word.label() == 'PERSON':
      named_entity = ' '.join(word[0] for word in chunked_word)
      entities.append(named_entity)
  return entities

space = 'John try to replicate the magic of Star Trek, but none have succeeded.'

print(f"\nName  Entities in 'space' using hasattr(): {find_NEs_pretty2(space)}")