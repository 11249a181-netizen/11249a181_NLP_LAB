import re

training_corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
test_sentence = "the fox flies over the house"
def tokenize(text):
    return re.findall(
        r"[a-z']+",
        text.lower()
    )
training_vocabulary = set(
    tokenize(training_corpus)
)
test_tokens = tokenize(test_sentence)
oov_words = [
    word
    for word in test_tokens
    if word not in training_vocabulary
]
oov_rate = (
    len(oov_words) / len(test_tokens)
) * 100
print("Training Vocabulary:")
print(training_vocabulary)
print("\nTest Sentence:")
print(test_sentence)
print("\nOOV Words:")
print(oov_words)
print("\nTotal Test Words:", len(test_tokens))
print("OOV Words:", len(oov_words))
print(f"OOV Rate: {oov_rate:.2f}%")