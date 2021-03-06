import numpy as np
import pandas as pd

sentences = """Thomas Jefferson began building Monticello at the age and of 26.
Construction was done mostly by local the masons and carpenters.
He moved into the South Pavilion in 1770.
Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

corpus = {}
for i, sent in enumerate(sentences.split('\n')):
  corpus['sent{}'.format(i)] = dict((tok,1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T

print(df[df.columns[:]])

#calcular produto escalar
df = df.T
print(df.sent0.dot(df.sent1))
print(df.sent0.dot(df.sent2))
print(df.sent0.dot(df.sent3))

print([(k, v) for (k, v) in (df.sent0 & df.sent1).items() if v])
print([(k, v) for (k, v) in (df.sent0 & df.sent2).items() if v])
print([(k, v) for (k, v) in (df.sent0 & df.sent3).items() if v])
