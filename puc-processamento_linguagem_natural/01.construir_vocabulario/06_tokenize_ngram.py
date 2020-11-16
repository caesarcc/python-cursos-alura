import re
from nltk.util import ngrams

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
pattern = re.compile(r"([-\s.,;!?])+")

tokens = pattern.split(sentence)
tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']

print(tokens)

tokens = list(ngrams(tokens, 2))

print(tokens)
