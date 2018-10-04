from nltk.corpus import brown

must_next = nltk.Index((t2, w2) for sentence in brown.tagged_sents() 
	for (w1, t1), (w2, t2) in nltk.bigrams(sentence) if (w1.lower() == 'must'))

for (tag, word_list) in must_next.items(): 
	print(tag, len(word_list))