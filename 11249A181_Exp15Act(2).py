from nltk import word_tokenize
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),       # your cue 1
    (r'.*ous$', 'JJ'),      # your cue 2
    (r'.*al$', 'JJ'),       # your cue 3
    (r'.*s$', 'NNS'),       # your cue 4
    (r'.*the.*', 'DT'),     # your cue 5
    (r'.*', 'NN'),          # default tag
]

tagger = RegexpTagger(patterns)

paragraph = "The scientists carefully examined the newly discovered species. They quickly noted its unusual behaviour and recorded their findings in a detailed report."

tokens = word_tokenize(paragraph)
print(tagger.tag(tokens))