import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
# Activity 1: POS tag a simple sentence
print("ACTIVITY 1: POS TAGGING")
sentence = "Ravi plays cricket every evening."
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)
print(tags)
for word, tag in tags:
    if tag.startswith('NN'):
        print(word, "- Noun")
    elif tag.startswith('VB'):
        print(word, "- Verb")
    elif tag.startswith('RB'):
        print(word, "- Adverb")
# Activity 2: Compare sentences
print("\nACTIVITY 2: COMPARE SENTENCES")
sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]
for sentence in sentences:
    print("\nSentence:", sentence)
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    print(tags)
    for word, tag in tags:
        if tag.startswith('NN'):
            category = "Noun"
        elif tag.startswith('VB'):
            category = "Verb"
        elif tag.startswith('JJ'):
            category = "Adjective"
        elif tag.startswith('RB'):
            category = "Adverb"
        elif tag.startswith('PRP'):
            category = "Pronoun"
        elif tag.startswith('DT'):
            category = "Determiner"
        else:
            category = "Other"
        print(word, "-", category)
# Activity 3: Context-dependent tagging
print("\nACTIVITY 3: CONTEXT-DEPENDENT TAGGING")
sentences = [
    "I read a book.",
    "Please book a ticket.",
    "Children play football.",
    "We watched a play."
]
for sentence in sentences:
    print("\nSentence:", sentence)
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    print(tags)
