import nltk
from nltk.corpus import ppattach

def pp_features(pp):
	return {'noun1': pp.noun1, 'noun2': pp.noun2}

phrases = [pp for pp in ppattach.attachments('training') if pp.attachment == 'N']

featuresets = [(pp_features(pp), pp.prep) for pp in phrases]
train_set, test_set = featuresets[1000:], featuresets[:1000]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(10))

classifier = nltk.MaxentClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(10))