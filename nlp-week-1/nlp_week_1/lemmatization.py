from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from pprint import pprint
from nltk import pos_tag
from nltk.corpus import wordnet

positive_quote = 'Better days are on their way, so stay positive. lemmatization classification'
positive_quote_words = word_tokenize(positive_quote)

lemmatizer = WordNetLemmatizer()

positive_quote_lemmatized_words = [lemmatizer.lemmatize(element) for element in positive_quote_words]
print(f"\nList of Words in 'positive_quote': {positive_quote_words}")
print(f"List of Lemmas in 'positive_quote': {positive_quote_lemmatized_words}")





#variation
print(f"\nLemma of the Noun 'better' (default: pos = 'n'): {lemmatizer.lemmatize('better')}")
print(f"Lemma of the Adjective 'better': {lemmatizer.lemmatize('better', pos='a')}")

def wordnet_pos(word):
  tag = pos_tag([word])[0][1][0].upper()
  tag_dict = {"N": wordnet.NOUN,
              "J": wordnet.ADJ,
              "V": wordnet.VERB,
              "R": wordnet.ADV}
  return tag_dict.get(tag, wordnet.NOUN)

print(f"\nList of Words in 'positive_quote': {positive_quote_words}")
print(f"List of Lemmas (Using POS Tags) in 'positive_quote': {[lemmatizer.lemmatize(word, wordnet_pos(word)) for word in word_tokenize(positive_quote)]}")



def pos_lemmatize_pprint(text):
  words = word_tokenize(text)
  lemmatized_words = [lemmatizer.lemmatize(word, wordnet_pos(word)) for word in words]
  print('Original Word : Lemma')
  pprint({words[word] : lemmatized_words[word] for word in range(len(lemmatized_words))}, indent = 10, depth = 5)

print("\nList of Lemmas (Using POS Tags) in 'positive_quote' with pprint:")
pos_lemmatize_pprint(positive_quote)