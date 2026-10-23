import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger, word_tokenize
nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')
tagged_sentences = brown.tagged_sents(categories='news')
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
sentence1 = "I saw her duck under the table and duck the flying ball."
tokens1 = word_tokenize(sentence1)
tagged1 = bigram_tagger.tag(tokens1)
print("\n1. Ambiguous Word - Duck")
print(tagged1)
for word, tag in tagged1:
    if word.lower() == "duck":
        print("duck ->", tag)
sentence2 = "The zibber runs quickly across the garden."
tokens2 = word_tokenize(sentence2)
tagged2 = bigram_tagger.tag(tokens2)
print("\n2. Unknown Word - Zibber")
print(tagged2)
for word, tag in tagged2:
    if word.lower() == "zibber":
        print("zibber ->", tag)
tweet = "OMG this movie is lit 😂"
poem = "The moon dances softly through the silent sky."
print("\n3. Tweet Tagging")
print(bigram_tagger.tag(word_tokenize(tweet)))
print("\nPoem Tagging")
print(bigram_tagger.tag(word_tokenize(poem)))
print("\n4. Issues in POS Tagging")
print("1. Duck: Ambiguity; the same word can have different meanings.")
print("2. Zibber: Unknown word; the tagger has not seen it during training.")
print("3. Tweet and poem: Domain mismatch can cause incorrect tags.")
