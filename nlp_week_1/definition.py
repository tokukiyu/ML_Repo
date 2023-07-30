from nltk.corpus import wordnet

defn=wordnet.synset('vehicle.n.01').definition();
#print(defn)

defn=wordnet.synset('vehicle.n.01').lemma_names()
defn=wordnet.lemma(defn)
print(defn)