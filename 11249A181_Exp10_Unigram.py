import re
from collections import Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)

tokens = tokenize(corpus)
N = len(tokens)
unigram_counts = Counter(tokens)

print("Total tokens (N):", N)
print(f"{'Word':<12}{'Count':<8}{'P(word)':<10}")
print("-" * 30)

for word, count in unigram_counts.most_common():
    probability = count / N
    print(f"{word:<12}{count:<8}{probability:<10.4f}")

def unigram_probability(word):
    return unigram_counts[word.lower()] / N

test_word = "fox"
print(f"\nP('{test_word}') = {unigram_probability(test_word):.4f}")