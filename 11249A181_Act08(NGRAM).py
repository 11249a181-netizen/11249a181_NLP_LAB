import re
import matplotlib.pyplot as plt
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
tokens = re.findall(
    r"[a-z']+",
    corpus.lower()
)
unigram_counts = Counter(tokens)
top10 = unigram_counts.most_common(10)
words = [
    item[0]
    for item in top10
]
frequencies = [
    item[1]
    for item in top10
]
plt.figure(figsize=(10, 6))
plt.bar(
    words,
    frequencies,
    color="skyblue"
)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigram Frequencies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()