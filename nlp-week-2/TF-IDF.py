from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import string
 
# documents = ['The dog plays with the ball', 'The cat plays with the ball']
documents = ['The dog plays fetch', 'The cat hunts bugs']
# Create Tokens from the set of documents
all_words = []
for document in documents:
    all_words.extend(word_tokenize(document))

## remove duplicates so only UNIQUE words remain
all_words_lower_case = [word.lower() for word in all_words]
unique_words = sorted(list(set(all_words_lower_case)))

## Process out stop words to create VOCABULARY
stop_words = set(stopwords.words('english'))
unique_words = filter(lambda word: word not in string.punctuation, unique_words)
vocabulary = [element for element in unique_words if element.casefold() not in stop_words]

total_documents = len(documents)
vectors = []
for document in documents:
  doc_vec = np.zeros((len(vocabulary),)) # create vector of all 0's
  index = 0 # tracks which vocabulary word we are on as vector index
  for word in vocabulary:
# calculate TF
        occurences = len([token for token in document.split() if token.lower() == word])
        words_in_doc = len(document.split())
        tf = float(occurences/words_in_doc)     

# calculate IDF
occurences = 0
for inner_document in documents:
    if word in inner_document.lower():
      occurences += 1

idf = np.log10(total_documents/occurences)

    # store IDF into the vector
doc_vec[index] = tf * idf
index += 1

  # inside outer loop but not inner loop
vectors.append(doc_vec) 

# outside both loops

print("{0} \n{1}\n".format(vocabulary,np.array(vectors)))
