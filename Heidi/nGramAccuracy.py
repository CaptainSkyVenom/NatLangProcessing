import nltk
from nltk.corpus import conll2000
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

bigram_chunker = BigramChunker(train_sents)
#print(bigram_chunker.evaluate(test_sents).incorrect()[:10])
i = 0
for correct in test_sents:   
     guess = bigram_chunker.parse(correct.leaves())  
     if correct != guess and i < 15:
        print(i, "\ncorrect: \n", correct, "\nguess: \n", guess) 
        i += 1     
#print(bigram_chunker.evaluate(test_sents).missed())
