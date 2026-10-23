import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
grammar = r"""
    NP: {<DT|PRP\$>?<RB.*>*<JJ.*>*<NN.*|NNS|NNP>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
def chunk_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged_words)
    print("\nSentence:", sentence)
    print("POS Tags:", tagged_words)
    print("Chunk Tree:", tree)
print("\n========== ACTIVITY 1 ==========")
sentences1 = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]
for sentence in sentences1:
    chunk_sentence(sentence)
print("\n========== ACTIVITY 2 ==========")
sentence2 = "The teacher explains the lesson in the classroom."
chunk_sentence(sentence2)
print("\n========== ACTIVITY 3 ==========")
sentence3 = "The young researcher develops an AI model."
chunk_sentence(sentence3)
print("\n========== ACTIVITY 4 ==========")
sentences4 = [
    "a student",
    "the very intelligent student"
]
for sentence in sentences4:
    chunk_sentence(sentence)