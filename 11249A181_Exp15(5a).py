
# Program 5(a): PoS Tagging using Hidden Markov Model (NLTK HMM)

import nltk
from nltk.corpus import brown
from nltk.tag import hmm

nltk.download('brown')

# Load tagged sentences from the Brown corpus
tagged_sentences = brown.tagged_sents(categories='news')

# Split into training and testing data (90% / 10%)
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

# Train an HMM tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(train_data)

# Evaluate accuracy
print(f"HMM Tagger Accuracy: {hmm_tagger.accuracy(test_data) * 100:.2f}%")

# Tag a new sentence
sentence = "They refuse to permit the strike".split()
print("\nTagged Output:", hmm_tagger.tag(sentence))