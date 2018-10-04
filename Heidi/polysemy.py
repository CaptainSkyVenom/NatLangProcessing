from nltk.corpus import wordnet as wn

def avg_polysemy(category):
	num_words = 0
	sum_sense = 0
	for synset in wn.all_synsets(category):
		num_words += 1
		sum_sense += len(wn.synsets(synset.lemmas()[0].name(), category))
	return sum_sense/num_words

for category in ['n', 'v', 'a', 'r']:
	print(category, avg_polysemy(category))