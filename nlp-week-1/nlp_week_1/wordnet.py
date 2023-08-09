from nltk.corpus import wordnet
hello_synset = wordnet.synsets('hello')
print(f"\nThe Synonym Set for the word 'hello' is: {hello_synset} \n")

hello_lemma_names = wordnet.synset('hello.n.01').lemma_names()
print(f"\nThe Lemma Names in the Synonym Set 'hello.n.01' are: {hello_lemma_names} \n")

hello_lemmas =  wordnet.lemmas('hello') 
print(f"\nThe Lemmas in the Word 'hello' are: {hello_lemmas} \n")

hello_n_01_synset_lemmas = wordnet.synset('hello.n.01').lemmas()
print(f"\nThe Lemmas in the Synonym Set 'hello.n.01' are: {hello_n_01_synset_lemmas} \n")

hello_n_01_hello_lemma_synset = wordnet.lemma('hello.n.01.hello').synset()
print(f"\nThe Synset for the Lemma 'hello.n.01.hello' is: {hello_n_01_hello_lemma_synset} \n")

hello_n_01_hello_lemma_synset_name = wordnet.lemma('hello.n.01.hello').name()
print(f"\nThe Word / Synset Name for the Lemma 'hello.n.01.hello' is: {hello_n_01_hello_lemma_synset_name} \n")


vehicle = wordnet.synset('vehicle.n.01')
types_of_vehicles = vehicle.hyponyms()
print(f'\nHyponyms / Types of Vehicles: {types_of_vehicles}')

wheeled_vehicle_n_01_hyponyms = wordnet.synset('wheeled_vehicle.n.01').hyponyms()
print(f"\nHyponyms of Hyponym 'wheeled_vehicle_n_01': {wheeled_vehicle_n_01_hyponyms}")