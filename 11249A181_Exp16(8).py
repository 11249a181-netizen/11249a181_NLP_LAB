import nltk
# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
# Input sentence
sentence = "The intelligent student reads a book."
# Tokenization
tokens = nltk.word_tokenize(sentence)
# POS tagging
tagged_words = nltk.pos_tag(tokens)
# Display output
print("Word\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t{tag}")
