from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["running", "better", "cars", "children"]
print("Word\t\tLemma")
for word in words:
    print(word, "\t\t", lemmatizer.lemmatize(word))