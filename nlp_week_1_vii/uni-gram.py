from nltk import UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

brown_unigram_tagger = UnigramTagger(brown_tagged_sents)

print(brown_unigram_tagger.tag(brown_sents[2009]))

print(brown_unigram_tagger.accuracy(brown_tagged_sents))
