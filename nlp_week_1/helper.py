from nltk.corpus import inaugural

def parse_year(addresses):
  return [year[0:4] for year in addresses]

def parse_president(addresses):
  presidents = []
  for president in addresses:
    dot_index = president.find('.')
    name = president[5:dot_index]
    presidents.append(name)
  return presidents

def calculate_length(addresses):
  lengths = []
  for address in addresses:
    words_punctuation = inaugural.words(address)
    just_words = [word for word in words_punctuation if word.isalpha()]
    length = len(just_words)
    lengths.append(length)
  return lengths

def combine_data(years, presidents, lengths):
  return tuple(zip(years, presidents, lengths))

def generate_table(addresses):
  years = parse_year(addresses)
  presidents = parse_president(addresses)
  lengths = calculate_length(addresses)
  table = combine_data(years, presidents, lengths)
  return table