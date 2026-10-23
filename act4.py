import nltk
from nltk.corpus import brown
from nltk import UnigramTagger
from nltk.tag import brill, brill_trainer
nltk.download('brown')
tagged_sentences = brown.tagged_sents(categories='news')
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
baseline_tagger = UnigramTagger(train_data)
templates = brill.brill24()
trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger,
    templates,
    trace=0
)
brill_tagger = trainer.train(train_data, max_rules=100)
print('Baseline accuracy:', baseline_tagger.accuracy(test_data))
print('Brill accuracy   :', brill_tagger.accuracy(test_data))