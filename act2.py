import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger
nltk.download('punkt')
nltk.download('punkt_tab')
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ous$', 'JJ'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]
tagger = RegexpTagger(patterns)
paragraph = "The little girl quickly finished her homework before dinner. The boys are playing happily."
tokens = word_tokenize(paragraph)
print(tagger.tag(tokens))