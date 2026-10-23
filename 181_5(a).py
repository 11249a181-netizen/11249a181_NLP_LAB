
import nltk
import numpy as np
from nltk.corpus import brown
from nltk.tag import hmm
# Fix missing NumPy reference in HMM module
hmm.np = np
# Download Brown corpus
nltk.download('brown')
# Load tagged sentences
tagged_sentences = brown.tagged_sents(categories='news')
# Split into training and testing data
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
# Train HMM tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(train_data)
# Evaluate accuracy
accuracy = hmm_tagger.accuracy(test_data)
print(f"HMM Tagger Accuracy: {accuracy * 100:.2f}%")
# Tag a sentence
sentence = "They refuse to permit the strike".split()
tagged_output = hmm_tagger.tag(sentence)
print("\nTagged Output:", tagged_output)
