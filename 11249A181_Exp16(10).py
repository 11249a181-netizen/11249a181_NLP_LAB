import nltk
# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
# Input sentence
sentence = "The intelligent student reads a book in the library."
# Tokenization and POS tagging
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS-tagged words:")
print(tagged_words)
# Define chunk grammar
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
# Create chunker
chunker = nltk.RegexpParser(grammar)
# Parse tagged words
chunk_tree = chunker.parse(tagged_words)
print("\nChunk tree:")
print(chunk_tree)
# Optional: display tree graphically
# chunk_tree.draw()
