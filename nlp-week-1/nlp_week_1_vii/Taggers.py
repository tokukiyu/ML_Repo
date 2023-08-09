from nltk import UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger, ConditionalFreqDist, trigrams, ConfusionMatrix
from nltk.corpus import brown
from pickle import dump, load

brown_sents = brown.sents(categories='reviews')
tagged_sents = brown.tagged_sents(categories='reviews')
print(tagged_sents[0])

tagged_sents_size = int(len(tagged_sents) * 0.9)
training_tagged_sents = tagged_sents[:tagged_sents_size]
testing_tagged_sents = tagged_sents[tagged_sents_size:]
print(testing_tagged_sents[0])

default_tagger = DefaultTagger('NN')
tagger1 = UnigramTagger(training_tagged_sents, backoff = default_tagger)
tagger2 = BigramTagger(training_tagged_sents, backoff = tagger1)
final_tagger = TrigramTagger(training_tagged_sents, backoff = tagger2)
print(tagger1, tagger2, final_tagger)


