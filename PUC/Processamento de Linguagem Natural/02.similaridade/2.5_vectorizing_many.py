from collections import Counter

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

docs = ["The faster Harry got to the store, the faster and faster Harry would get home."]
docs.append("Harry is hairy and faster than Jill.")
docs.append("Jill is not as hairy as Harry.")

doc_tokens = []
for doc in docs:
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
print(len(doc_tokens[0]))

all_doc_tokens = sum(doc_tokens, [])
print(len(all_doc_tokens))

lexicon = sorted(set(all_doc_tokens))
print(len(lexicon))

print(lexicon)

# calculando o vetor de mesma dimensão para cada documento
from collections import OrderedDict

zero_vector = OrderedDict((token, 0) for token in lexicon)
print(zero_vector)

import copy

doc_vectors = []
for doc in docs:
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    doc_vectors.append(vec)

print (len(doc_vectors))
print (doc_vectors[0])

# calculando a distância dos cossenos para os vetores de cada documento
import math


def cosine_sim(vec1, vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]

    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]

    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))

    return dot_prod / (mag_1 * mag_2)

d = cosine_sim(doc_vectors[0], doc_vectors[2])
print("cosine_sim:", d)
