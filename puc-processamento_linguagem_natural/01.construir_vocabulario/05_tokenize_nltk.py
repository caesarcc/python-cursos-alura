from nltk.tokenize.casual import casual_tokenize

message = """RT TJMonticello Best day everrrrrrr at Monticello. Awesommmmmmeeeeeeee day"""

tokens = casual_tokenize(message)
print(tokens)

tokens = casual_tokenize(message, preserve_case=False, reduce_len=True, strip_handles=True)
print(tokens)
