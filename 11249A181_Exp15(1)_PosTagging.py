import nltk
from nltk import word_tokenize, pos_tag  # import the tokenizer and tagger functions

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The little girl quickly finished her homework before dinner."

tokens = word_tokenize(sentence)  # Step 1: tokenize the sentence
tagged = pos_tag(tokens)           # Step 2: PoS-tag the tokens

for word, tag in tagged:
    print(word, "->", tag)