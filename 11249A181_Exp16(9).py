import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
# Input sentence
sentence = "The boy plays in the garden."
# Tokenization and POS tagging
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS Tagged Words:")
print(tagged_words)
# Grammar for chunking
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
# Create chunk parser
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("\nChunk Tree:")
print(chunk_tree)
