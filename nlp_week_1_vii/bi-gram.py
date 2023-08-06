from nltk import UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

brown_tagged_sents_size = int(len(brown_tagged_sents) * 0.9)
training_brown_tagged_sents = brown_tagged_sents[:brown_tagged_sents_size]
testing_brown_tagged_sents = brown_tagged_sents[brown_tagged_sents_size:]

brown_bigram_tagger = BigramTagger(training_brown_tagged_sents)
print(brown_bigram_tagger.tag(brown_sents[2009]))
print(brown_bigram_tagger.accuracy(testing_brown_tagged_sents))


brown_additional_sentences = brown_sents[4205]
print(brown_bigram_tagger.tag(brown_additional_sentences))
print(brown_bigram_tagger.accuracy(testing_brown_tagged_sents))


default_tagger = DefaultTagger('NN')
tagger1 = UnigramTagger(training_brown_tagged_sents, backoff = default_tagger)
tagger2 = BigramTagger(training_brown_tagged_sents, backoff = tagger1)
tagger3 = TrigramTagger(training_brown_tagged_sents, backoff = tagger2)

print(tagger3.accuracy(testing_brown_tagged_sents))