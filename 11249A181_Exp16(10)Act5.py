
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The very intelligent student reads a book."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

# Original grammar
grammar1 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

chunker1 = nltk.RegexpParser(grammar1)
tree1 = chunker1.parse(tagged_words)

print("Original Chunk Tree:")
print(tree1)

# Improved grammar: allow adverbs before adjectives
grammar2 = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""

chunker2 = nltk.RegexpParser(grammar2)
tree2 = chunker2.parse(tagged_words)

print("\nImproved Chunk Tree:")
print(tree2)

