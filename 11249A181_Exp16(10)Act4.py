
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The student reads a book in the library.",
    "The professor teaches computer science.",
    "A student walks to the classroom.",
    "The researchers work in the laboratory.",
    "The librarian arranges the books on the shelf."
]

grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged_words)

    print("\nSentence:", sentence)
    print(tree)
