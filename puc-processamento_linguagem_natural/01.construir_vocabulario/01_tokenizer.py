import numpy as np
import pandas as pd

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
tokens = str.split(sentence)
vocab = sorted(set(tokens))

onehot_vectors = np.zeros((len(tokens), len(vocab)), int)

for i, word in enumerate(tokens):
    onehot_vectors[i, vocab.index(word)] = 1

print(onehot_vectors)

print(pd.DataFrame(onehot_vectors, columns=vocab))
