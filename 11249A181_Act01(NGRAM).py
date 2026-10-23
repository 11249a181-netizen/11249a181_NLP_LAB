import re
from nltk import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
tokens = re.findall(r"[a-z']+", corpus.lower())
fdist = FreqDist(tokens)
N = len(tokens)
print("Total tokens:", N)
print(f"{'Word':<12}{'Count':<8}{'Probability':<12}")
print("-" * 32)
for word, count in fdist.most_common():
    probability = count / N
    print(f"{word:<12}{count:<8}{probability:<12.4f}")
word = "fox"
print(f"\nP('{word}') = {fdist[word] / N:.4f}")