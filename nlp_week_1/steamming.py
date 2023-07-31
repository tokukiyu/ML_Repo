from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import LancasterStemmer
from nltk.stem import SnowballStemmer

paper_grade = 'I am fairly certain that I will get an A on my paper. classified classificationer necessity'

paper_grade_words = word_tokenize(paper_grade)
porter_stemmers = PorterStemmer()

paper_grade_stemmed_words = [porter_stemmers.stem(element) for element in paper_grade_words]
print(f"\nList of Words in 'paper_grade': {paper_grade_words}")
print(f"\nList of Stems in 'paper_grade' using the PorterStemmer() Method: {paper_grade_stemmed_words}")

lancaster_stemmer = LancasterStemmer()
paper_grade_stemmed_words2 = [lancaster_stemmer.stem(element) for element in paper_grade_words]
print(f"\nList of Stems in 'paper_grade' using the LancasterStemmer() Method: {paper_grade_stemmed_words2}")


Snowball_Stemmer = SnowballStemmer('english')
paper_grade_stemmed_words2 = [Snowball_Stemmer.stem(element) for element in paper_grade_words]
print(f"\nList of Stems in 'paper_grade' using the SnowballStemmer() Method: {paper_grade_stemmed_words2}")



bread = 'Before we had rubber erasers, we erased graphite with rolled-up white bread.'
snowball_stemmer = SnowballStemmer('english', ignore_stopwords = True/False)
bread_stemmed_words = [snowball_stemmer.stem(element) for element in word_tokenize(bread)]
print(f"\nList of Stems in 'bread' using the SnowballStemmer() Method: {bread_stemmed_words}")

snowball_stemmer_ignore_stopwords = SnowballStemmer('english', ignore_stopwords = True)
bread_stemmed_words_ignore_stopwords = [snowball_stemmer_ignore_stopwords.stem(element) for element in word_tokenize(bread)]
print(f"\nList of Stems in 'bread' using the SnowballStemmer() Method Without Stemming Stop Words: {bread_stemmed_words_ignore_stopwords}")