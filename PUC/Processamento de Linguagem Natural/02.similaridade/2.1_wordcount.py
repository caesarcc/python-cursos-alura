from collections import Counter

from nltk.tokenize import TreebankWordTokenizer

sentence = """The faster Harry got to the store, the faster Harry, the faster, would get home."""

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
print(tokens)

bag_of_words = Counter(tokens)
print(bag_of_words)

bag_of_words_most_common = bag_of_words.most_common(4)
print(bag_of_words_most_common)

times_harry_appears = bag_of_words['harry']
num_unique_words = len(bag_of_words)
tf = times_harry_appears / num_unique_words
print(round(tf, 4))

print('{} tokens, {} unicos'.format(len(tokens), num_unique_words))


