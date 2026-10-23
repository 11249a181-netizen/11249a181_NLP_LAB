
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The young researcher develops an AI model."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

print("POS Tagged Sequence:")
print(tagged_words)

grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)

print("\nNoun Phrases:")
print(chunk_tree)
