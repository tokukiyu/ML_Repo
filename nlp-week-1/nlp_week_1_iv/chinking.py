from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

medal_quote = "These boys collected the bronze medal for third team place and were only ten points away from earning a gold medal."
medal_quote_tokens = word_tokenize(medal_quote)
medal_quote_tags = pos_tag(medal_quote_tokens)

chunk_grammar_noJJ = """NoAdjChunk: {<.*>+}
                        }<JJ>{"""
chunk_parser_noJJ = RegexpParser(chunk_grammar_noJJ)
medal_quote_chunked = chunk_parser_noJJ.parse(medal_quote_tags)
print("\nChunked 'medal_quote' without Adjectives: \n", medal_quote_chunked)