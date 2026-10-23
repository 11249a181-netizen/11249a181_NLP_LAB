import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence1 = "The young scientist is developing a new application."
sentence2 = "The students read their textbooks."
sentence3 = "The boy plays in the garden."
campus_sentences = [
    "The student reads a book in the library.",
    "The teacher explains the lesson in the classroom.",
    "A clever student solves the problem.",
    "The students play in the playground.",
    "The researcher develops a new application in the laboratory."
]
sentence5 = "The very intelligent student reads a book."
def run_chunker(sentence, grammar):
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print("\nSentence:", sentence)
    print("POS Tags:", tagged_words)
    chunker = nltk.RegexpParser(grammar)
    tree = chunker.parse(tagged_words)
    print("Chunk Tree:")
    print(tree)
    return tree
basic_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
extended_grammar = r"""
    NP: {<DT|PRP\$>?<RB.*>*<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
print("\n========== ACTIVITY 1 ==========")
run_chunker(sentence1, basic_grammar)
print("\n========== ACTIVITY 2 ==========")
run_chunker(sentence2, extended_grammar)
print("\n========== ACTIVITY 3: NP ONLY ==========")
np_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
run_chunker(sentence3, np_grammar)
print("\n========== ACTIVITY 3: NP + VP + PP ==========")
run_chunker(sentence3, basic_grammar)
for sentence in campus_sentences:
    run_chunker(sentence, basic_grammar)
print("\n========== ACTIVITY 5: ERROR ANALYSIS ==========")
print("\nUsing basic grammar:")
run_chunker(sentence5, basic_grammar)
print("\nUsing improved grammar:")
run_chunker(sentence5, extended_grammar)
print("\nObservation:")
print("The basic grammar may miss adverbs inside noun phrases.")
print("The extended grammar allows adverbs before adjectives.")
print("Simple VP rules may split auxiliary and main verbs.")

