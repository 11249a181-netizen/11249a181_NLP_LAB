from nltk import PorterStemmer
from nltk import WordNetLemmatizer
ps = PorterStemmer()
lm = WordNetLemmatizer()
words = ('running', 'playing', 'talking', 'mice', 'leaves')
print(f"{'words':<15}{'stem':<15}{'lemma':<15}")
print("-" * 45)
for word in words:
    stem = ps.stem(word)
    lemma = lm.lemmatize(word)
    print(f"{word:<15}{stem:<15}{lemma:<15}")
