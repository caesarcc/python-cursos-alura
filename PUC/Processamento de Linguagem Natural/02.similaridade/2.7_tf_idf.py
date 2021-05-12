from nlpia.data.loaders import kite_text, kite_history
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

kite_intro = kite_text.lower()
intro_tokens = tokenizer.tokenize(kite_intro)
kite_history = kite_history.lower()
history_tokens = tokenizer.tokenize(kite_history)
intro_total = len(intro_tokens)
print(intro_total)

history_total = len(history_tokens)
print(history_total)

# calculando o TF de "kite" em cada documento
from collections import Counter

intro_tf = {}
history_tf = {}

intro_counts = Counter(intro_tokens)
intro_tf['kite'] = intro_counts['kite'] / intro_total

history_counts = Counter(history_tokens)
history_tf['kite'] = history_counts['kite'] / history_total

print('Term Frequency of "kite" in intro is: {:.4f}'.format(intro_tf['kite']))
print('Term Frequency of "kite" in history is: {:.4f}'.format(history_tf['kite']))

# calculando o TF da palavra "and"
intro_tf['and'] = intro_counts['and'] / intro_total
history_tf['and'] = history_counts['and'] / history_total
print('Term Frequency of "and" in intro is: {:.4f}'.format(intro_tf['and']))
print('Term Frequency of "and" in history is: {:.4f}'.format(history_tf['and']))

# calculando o número de documentos em que cada um dos três termos aparecem
num_docs_containing_and = 0
for doc in [intro_tokens, history_tokens]:
    if 'and' in doc:
        num_docs_containing_and += 1

num_docs_containing_kite = 0
for doc in [intro_tokens, history_tokens]:
    if 'kite' in doc:
        num_docs_containing_kite += 1

num_docs_containing_china = 0
for doc in [intro_tokens, history_tokens]:
    if 'china' in doc:
        num_docs_containing_china += 1

# calculando TF de "china" 
intro_tf['china'] = intro_counts['china'] / intro_total
history_tf['china'] = history_counts['china'] / history_total

print('Term Frequency of "china" in intro is: {:.4f}'.format(intro_tf['china']))
print('Term Frequency of "china" in history is: {:.4f}'.format(history_tf['china']))

# calculando o IDF para todos os três termos nos dois documentos
num_docs = 2
intro_idf = {}
history_idf = {}
intro_idf['and'] = num_docs / num_docs_containing_and
history_idf['and'] = num_docs / num_docs_containing_and
intro_idf['kite'] = num_docs / num_docs_containing_kite
history_idf['kite'] = num_docs / num_docs_containing_kite
intro_idf['china'] = num_docs / num_docs_containing_china
history_idf['china'] = num_docs / num_docs_containing_china

print(intro_idf['and'])
print(history_idf['and'])
print(intro_idf['kite'])
print(history_idf['kite'])
print(intro_idf['china'])
print(history_idf['china'])

# calculando o resultado para o documento "intro"
intro_tfidf = {}
intro_tfidf['and'] = intro_tf['and'] * intro_idf['and']
intro_tfidf['kite'] = intro_tf['kite'] * intro_idf['kite']
intro_tfidf['china'] = intro_tf['china'] * intro_idf['china']

# calculando o resultado para o documento "history"
history_tfidf = {}
history_tfidf['and'] = history_tf['and'] * history_idf['and']
history_tfidf['kite'] = history_tf['kite'] * history_idf['kite']
history_tfidf['china'] = history_tf['china'] * history_idf['china']

print(intro_tfidf['and'])
print(intro_tfidf['kite'])
print(intro_tfidf['china'])

print(history_tfidf['and'])
print(history_tfidf['kite'])
print(history_tfidf['china'])






