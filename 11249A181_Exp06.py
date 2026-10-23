from nltk.tokenize import sent_tokenize
text = "Hello everyone. Welcome to NLP Lab. Today we will learn tokenization."
sentences = sent_tokenize(text)
print("Sentence Tokens:")
for sentence in sentences:
    print(sentence)