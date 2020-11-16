from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

text = ' '.join([stemmer.stem(w).strip("'") for w in "dish washer's washed dishes".split()])

print(text)
