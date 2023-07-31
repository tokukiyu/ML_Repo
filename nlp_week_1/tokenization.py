from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize

lorenzo_paragraph = "Lorenzo di Piero de'Medici was an Italian statesman, banker, de facto ruler of the Florentine Republic and the most powerful and enthusiastic patron of Renaissance culture in Italy. Also known as Lorenzo the Magnificent (Lorenzo il Magnifico) by contemporary Florentines, he was a magnate, diplomat, politician and patron of scholars, artists,\
    and poets. As a patron, he's best known for his sponsorship of artists such as Botticelli and Michelangelo. He held the balance of power within the Italic League, \
    an alliance of states that stabilized political conditions on the Italian peninsula for decades, and his life coincided with the mature phase of the Italian Renaissance and the Golden Age of Florence."

#print(f'Tokenized Text by Word Using word_tokenize(): {word_tokenize(lorenzo_paragraph)}')
#print(f'Tokenized Text by Sentence Using sent_tokenize(): {sent_tokenize(lorenzo_paragraph)}')

a=sent_tokenize(lorenzo_paragraph)

for b in a:
    print (f"{b}")
