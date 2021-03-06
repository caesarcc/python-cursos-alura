from nltk.tokenize import TreebankWordTokenizer
from nlpia.data.loaders import kite_text
import nltk
from collections import Counter

tokenizer = TreebankWordTokenizer()

tokens = tokenizer.tokenize(kite_text.lower())
token_counts = Counter(tokens)

nltk.download('stopwords', quiet=True)
stopwords = nltk.corpus.stopwords.words('english')

tokens = [x for x in tokens if x not in stopwords]
kite_counts = Counter(tokens)

print(kite_counts)
