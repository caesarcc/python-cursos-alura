import nltk

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

print(len(stop_words))

stopwords = stop_words[:7]
print(stopwords)
