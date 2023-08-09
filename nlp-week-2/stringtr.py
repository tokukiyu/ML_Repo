import string

unique_words = ["hello", "world", ",", "programming", "is", "fun", "!"]
unique_words = filter(lambda word: word not in string.punctuation, unique_words)

filtered_words = list(unique_words)
print(filtered_words)  # Output: ['hello', 'world', 'programming', 'is', 'fun']
