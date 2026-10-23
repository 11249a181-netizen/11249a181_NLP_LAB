
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "a student",
    "the very intelligent student"
]

grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    chunk_tree = chunker.parse(tagged_words)

    print("\nSentence:", sentence)
    print("POS Tagged Sequence:", tagged_words)
    print("Chunk Structure:")
    print(chunk_tree)