import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("POS Tagged Words:")
print(tagged_words)
print("\nChunk Tree:")
print(chunk_tree)
