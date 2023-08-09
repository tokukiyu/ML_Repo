from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

choc_sentence = 'If I had a chocolate bar, I would eat one piece of it every hour.'
choc_sentence_words = word_tokenize(choc_sentence)
stop_words = set(stopwords.words('english'))
choc_sentence_filtered = [element for element in choc_sentence_words if element.casefold() not in stop_words]

print(f'\nChocolate Sentence, Original: {choc_sentence_words}')
print(f'\nChocolate Sentence, Filtered: {choc_sentence_filtered}')

stop_words_without_i_or_a = stop_words - {'i', 'a'}
choc_sentence_filtered_without_i_or_a = [element for element in choc_sentence_words if element.casefold() not in stop_words_without_i_or_a]
print(f"\nChocolate Sentence, Filtered Without Including 'i' or 'a': {choc_sentence_filtered_without_i_or_a}")


def not_stopwords_percentage(data):
  content = [element for element in data if element.casefold() not in stop_words]
  percentage = 100 * (len(content) / len(data))
  return(percentage)

print(f"\n Percentage of Words That Are NOT Stop Words in 'choc_sentence': {not_stopwords_percentage(choc_sentence)}%")

