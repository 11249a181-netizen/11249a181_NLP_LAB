import re
import random
from collections import Counter, defaultdict

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    return re.findall(r"[a-z']+", sentence.lower())

sentences = corpus.split("\n")

bigram_model = defaultdict(Counter)
trigram_model = defaultdict(Counter)

for sentence in sentences:

    words = tokenize(sentence)

    words = ["<s>", "<s>"] + words + ["</s>"]

    for i in range(len(words) - 1):
        bigram_model[words[i]][words[i + 1]] += 1

    for i in range(len(words) - 2):
        trigram_model[
            (words[i], words[i + 1])
        ][words[i + 2]] += 1


def generate_bigram(max_len=15):

    word = "<s>"
    result = []

    for _ in range(max_len):

        choices = bigram_model[word]

        if not choices:
            break

        words, counts = zip(*choices.items())

        word = random.choices(
            words,
            weights=counts
        )[0]

        if word == "</s>":
            break

        result.append(word)

    return " ".join(result)


def generate_trigram(max_len=15):

    w1 = "<s>"
    w2 = "<s>"
    result = []

    for _ in range(max_len):

        choices = trigram_model[(w1, w2)]

        if not choices:
            break

        words, counts = zip(*choices.items())

        w3 = random.choices(
            words,
            weights=counts
        )[0]

        if w3 == "</s>":
            break

        result.append(w3)

        w1 = w2
        w2 = w3

    return " ".join(result)


random.seed(42)

print("Bigram Generated Text")
print("-------------------------")

for i in range(3):
    print(generate_bigram())

print("\nTrigram Generated Text")
print("-------------------------")

for i in range(3):
    print(generate_trigram())