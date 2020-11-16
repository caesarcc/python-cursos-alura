import nltk
from sklearn.feature_extraction.text import \
    ENGLISH_STOP_WORDS as sklearn_stop_words

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

print(len(stop_words))

print(len(sklearn_stop_words))

print(sklearn_stop_words)


