# Activity: Perplexity computation

def perplexity(prob, n):
    return prob ** (-1 / n) if prob > 0 else float("inf")

test_sentence = "the fox runs away"
n = len(test_sentence.split())

uni_p = 0.0009
bi_p = 0.00021
tri_p = 0.00007

print("Test Sentence:", test_sentence)
print()

print(f"{'Model':<15}{'Sentence Probability':<25}{'Perplexity':<15}")
print("-" * 55)

print(f"{'Unigram':<15}{uni_p:<25.5f}{perplexity(uni_p, n):<15.2f}")
print(f"{'Bigram':<15}{bi_p:<25.5f}{perplexity(bi_p, n):<15.2f}")
print(f"{'Trigram':<15}{tri_p:<25.5f}{perplexity(tri_p, n):<15.2f}")