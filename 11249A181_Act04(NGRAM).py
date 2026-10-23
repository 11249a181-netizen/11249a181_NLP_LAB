import nltk
import re
from nltk.corpus import gutenberg
from collections import Counter
nltk.download("gutenberg")
words = gutenberg.words("austen-emma.txt")
tokens = [
    word.lower()
    for word in words
    if re.fullmatch(r"[a-zA-Z']+", word)
]
unigram_counts = Counter(tokens)
print("Total tokens:", len(tokens))
print("Vocabulary size:", len(unigram_counts))
print("\nTop 20 Unigrams")
print("-------------------------")
for word, count in unigram_counts.most_common(20):
    probability = count / len(tokens)
    print(
        f"{word:<15}{count:<8}{probability:.6f}"
    )
bigrams = Counter(
    zip(tokens, tokens[1:])
)
print("\nTop 20 Bigrams")
print("-------------------------")
for bigram, count in bigrams.most_common(20):
    print(f"{bigram!s:<35}{count}")
trigrams = Counter(
    zip(tokens, tokens[1:], tokens[2:])
)
print("\nTop 20 Trigrams")
print("-------------------------")
for trigram, count in trigrams.most_common(20):
    print(f"{trigram!s:<50}{count}")