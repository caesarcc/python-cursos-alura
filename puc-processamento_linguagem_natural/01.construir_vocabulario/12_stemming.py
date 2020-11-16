import re 

def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$', word)[0][0].strip("'") for word in phrase.lower().split()])

print(stem('houses'))

print(stem("Doctor House's calls"))
