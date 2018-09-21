from nltk.corpus import wordnet as wn
noun_count = 0
total_noun_count = 0
for synset in wn.all_synsets('n'):
    #print(synset.name()[:-5])
    total_noun_count += 1
    noun_count += len(wn.synsets(synset.name()[:-5],'n'))
print(noun_count, total_noun_count, noun_count/total_noun_count)
