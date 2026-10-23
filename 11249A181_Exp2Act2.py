from collections import Counter
corpus = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]
unigram = Counter()
bigram = Counter()
total_words = 0
for sentence in corpus:
    words = sentence.split()
    total_words += len(words)
    unigram.update(words)
    for i in range(len(words) - 1):
        bigram[(words[i], words[i + 1])] += 1
print("Unigram Probability:")
for word, count in unigram.items():
    print(f"P({word}) = {count}/{total_words} = {count/total_words:.3f}")
print("\nBigram Probability:")
for (w1, w2), count in bigram.items():
    print(f"P({w2}|{w1}) = {count}/{unigram[w1]} = {count/unigram[w1]:.3f}")