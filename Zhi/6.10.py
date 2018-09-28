from nltk.corpus import brown
import nltk
featuresets = []
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (w1.lower() == 'in' and (t2.startswith('DT') or t2 == 'AT') and t3.startswith('N')):
            featuresets.append(({'word':w3}, 'in'))
            #print(w1, w2, w3)
        if (w1.lower() == 'on' and (t2.startswith('DT') or t2 == 'AT') and t3.startswith('N')):
            featuresets.append(({'word':w3}, 'on'))
            #print(w1, w2, w3)

        # if w1.lower() == 'on' and (t2.startswith('DT') or t2 == 'AT') and w3.lower() == 'computer':
        #     #featuresets.append(({'word':w3}, 'on'))
        #     print(sentence)
    



for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(classifier.show_most_informative_features(10))
#print(nltk.classify.accuracy(classifier, test_set))
print(classifier.classify({'word':input("Enter the word please: ").lower()}))
