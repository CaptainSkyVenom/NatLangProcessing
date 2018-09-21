import matplotlib.pyplot as plt
import nltk
import random
from nltk.corpus import gutenberg
gutenberg.fileids()
#emma = gutenberg.words('austen-emma.txt')

n = 1000
s = ""
for i in range(100000000):
    s += random.choice("abcdefg ")
emma = s.split()

fdist = nltk.FreqDist(w.lower() for w in emma if w.isalpha())
wordlist = []
for word in fdist:
    wordlist.append((word, fdist[word]))
sorted_by_second = sorted(wordlist, key=lambda tup: tup[1])[::-1]

x,y = zip(*sorted_by_second)
plt.plot(list(range(1, len(wordlist)+1)), y)
plt.yscale('log')
plt.xscale('log')
#plt.ylabel('some numbers')
plt.show()
