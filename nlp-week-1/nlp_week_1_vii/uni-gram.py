from nltk import UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

brown_unigram_tagger = UnigramTagger(brown_tagged_sents)

print(brown_unigram_tagger.tag(brown_sents[2009]))

print(brown_unigram_tagger.accuracy(brown_tagged_sents))

brown_tagged_sents_size = int(len(brown_tagged_sents) * 0.9)
training_brown_tagged_sents = brown_tagged_sents[:brown_tagged_sents_size]
testing_brown_tagged_sents = brown_tagged_sents[brown_tagged_sents_size:]
brown_unigram_tagger2 = UnigramTagger(training_brown_tagged_sents)
print(brown_unigram_tagger2.accuracy(testing_brown_tagged_sents))