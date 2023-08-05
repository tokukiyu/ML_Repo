from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
coffee = "Angela Merkel grabbed the cup of coffee and took a sip as she stepped around the corner of Starbucks."

coffee_tokens = word_tokenize(coffee)
coffee_tags = pos_tag(coffee_tokens)

coffee_NEs = ne_chunk(coffee_tags)
print(f"\nName Entities in 'coffee': {coffee_NEs}")