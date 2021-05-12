from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from nlpia.data.loaders import kite_text

tokenizer = TreebankWordTokenizer()

tokens = tokenizer.tokenize(kite_text.lower())
token_counts = Counter(tokens)
print(token_counts)


