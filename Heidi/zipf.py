import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
import random

emma = gutenberg.words('austen-emma.txt')

num = 50

def zipf(text):
	
	fdist = nltk.FreqDist(text)
	fdist = fdist.most_common(num)

	plt.plot(range(len(fdist)), [freq for word, freq in fdist])
	plt.xscale('log')
	plt.yscale('log')
	plt.show()

#zipf(emma)

rand_text = ''

for i in range(1000000):
	rand_text += random.choice("abcdefg ")

rand_text = rand_text.split()

zipf(rand_text)

