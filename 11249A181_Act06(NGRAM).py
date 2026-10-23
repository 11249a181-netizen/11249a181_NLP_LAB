import re
from collections import Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    return ["<s>"] + re.findall(
        r"[a-z']+",
        sentence.lower()
    ) + ["</s>"]

sentences = [
    tokenize(s)
    for s in corpus.split("\n")
]

bigram_counts = Counter()
context_counts = Counter()

vocab = set()

for sentence in sentences:

    vocab.update(sentence)

    for i in range(len(sentence) - 1):

        w1 = sentence[i]
        w2 = sentence[i + 1]

        bigram_counts[(w1, w2)] += 1
        context_counts[w1] += 1

V = len(vocab)

def bigram_probability(w1, w2, k):

    return (
        bigram_counts[(w1, w2)] + k
    ) / (
        context_counts[w1] + k * V
    )

def sentence_probability(sentence, k):

    tokens = tokenize(sentence)
    probability = 1.0

    for i in range(len(tokens) - 1):

        probability *= bigram_probability(
            tokens[i],
            tokens[i + 1],
            k
        )

    return probability

test_sentence = "the fox runs"

print("Sentence:", test_sentence)
print()

print(f"{'k':<10}{'Sentence Probability':<25}")
print("-" * 35)

for k in [0.01, 0.1, 0.5, 1, 2, 5]:

    probability = sentence_probability(
        test_sentence,
        k
    )

    print(
        f"{k:<10}"
        f"{probability:<25.10f}"
    )