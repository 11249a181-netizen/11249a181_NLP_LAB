from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "played", "studies", "playing", "better"]
print(" Word \t\tStem")
for word in words:
    print(word, "\t", ps.stem(word))