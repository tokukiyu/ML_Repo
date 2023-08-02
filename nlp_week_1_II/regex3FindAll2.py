import re
from re import finditer

art_sentences = ['There is no greater joy for an artist than to know their work is in the hands of someone who truly understands it.',
                 'These guys have state of the art equipment.']

pattern3 = ['art', 'artist', 'dog']

for art_sentence in art_sentences:
    for each_pattern3 in pattern3:
        if re.findall(each_pattern3, art_sentence):
            for each_pattern_found in finditer(each_pattern3,
                                               art_sentence):
                print(
                    f'\n Match! Location: {each_pattern_found.span()}. The pattern "{each_pattern_found.group()}" is in the sentence: "   {art_sentence}"')
        else:
            print(
                f'\nNo Match! The pattern "{each_pattern3}" is not in the sentence: "{art_sentence}"')
