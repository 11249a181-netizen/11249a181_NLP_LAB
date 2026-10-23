
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The teacher explains the lesson in the classroom."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

np_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

full_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

print("NP Only:")
print(nltk.RegexpParser(np_grammar).parse(tagged_words))

print("\nNP + VP + PP:")
print(nltk.RegexpParser(full_grammar).parse(tagged_words))
