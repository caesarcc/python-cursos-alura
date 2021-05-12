import nltk
from nltk.corpus.reader.wordnet import VERB

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("made", pos=VERB))
print(lemmatizer.lemmatize("good", pos="a"))
print(lemmatizer.lemmatize("goods", pos="a"))
print(lemmatizer.lemmatize("goods", pos="n"))
print(lemmatizer.lemmatize("goodness", pos="n"))
print(lemmatizer.lemmatize("best", pos="a"))


