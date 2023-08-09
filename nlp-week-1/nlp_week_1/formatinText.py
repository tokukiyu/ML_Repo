from nltk.corpus import inaugural
from helper import generate_table

def print_table(data):
  print(f"{'Year': <8}{'President': <14}{'Length'}")
  print(f"{'----': <8}{'---------': <14}{'------'}")
  for d in data:
    print(f'{d[0]: <8}{d[1]: <14}{d[2]}')

inaugural_addresses = inaugural.fileids()
info = generate_table(inaugural_addresses)
print_table(info)

from nltk.corpus import inaugural

with open('bush_1989_address.txt', 'w') as writer:
  address_words = inaugural.words('1989-Bush.txt')
  lowercase_list = [word.lower() for word in address_words if word.isalpha()]
  lowercase_set = set(lowercase_list)
  writer.writelines([word + '\n' for word in sorted(lowercase_set)])
  
  
  from nltk.corpus import inaugural

with open('bush_sentences.txt', 'w') as writer:
  address_sentences_list = inaugural.sents('1989-Bush.txt')
  address_sentences = [f"{' '.join(sentence)}\n" for sentence in address_sentences_list]
  writer.writelines(address_sentences)