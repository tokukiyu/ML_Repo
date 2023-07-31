from nltk.corpus import stopwords
from nltk.corpus import names
from nltk.corpus import cmudict
import nltk
inaugural_corpus_words = nltk.corpus.inaugural.words()

def stopwords_percentage(data):
  english_stopwords = stopwords.words('english')
  content = [element for element in data if element.lower() in english_stopwords]
  return(100 * (len(content) / len(data)))

male_names = names.words('male.txt')

male_names_startingwith_Za = [element for element in male_names if element.startswith('Za')]
print(f"\nMale Names Starting with 'Za' in the Names Lexicon Corpus : {male_names_startingwith_Za}")