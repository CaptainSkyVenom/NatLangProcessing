from nltk.corpus import brown
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tag import NgramTagger
import nltk

class minus1gramTagger(NgramTagger):
    """
    Unigram Tagger
    The UnigramTagger finds the most likely tag for each word in a training
    corpus, and then uses that information to assign tags to new tokens.
        >>> from nltk.corpus import brown
        >>> from nltk.tag import UnigramTagger
        >>> test_sent = brown.sents(categories='news')[0]
        >>> unigram_tagger = UnigramTagger(brown.tagged_sents(categories='news')[:500])
        >>> for tok, tag in unigram_tagger.tag(test_sent):
        ...     print("(%s, %s), " % (tok, tag))
        (The, AT), (Fulton, NP-TL), (County, NN-TL), (Grand, JJ-TL),
        (Jury, NN-TL), (said, VBD), (Friday, NR), (an, AT),
        (investigation, NN), (of, IN), (Atlanta's, NP$), (recent, JJ),
        (primary, NN), (election, NN), (produced, VBD), (``, ``),
        (no, AT), (evidence, NN), ('', ''), (that, CS), (any, DTI),
        (irregularities, NNS), (took, VBD), (place, NN), (., .),
    :param train: The corpus of training data, a list of tagged sentences
    :type train: list(list(tuple(str, str)))
    :param model: The tagger model
    :type model: dict
    :param backoff: Another tagger which this tagger will consult when it is
        unable to tag a word
    :type backoff: TaggerI
    :param cutoff: The number of instances of training data the tagger must see
        in order not to use the backoff tagger
    :type cutoff: int
    """

    json_tag = 'nltk.tag.sequential.UnigramTagger'

    def __init__(self, train=None, model=None,
                 backoff=None, cutoff=0, verbose=False):
        NgramTagger.__init__(self, 1, train, model,
                             backoff, cutoff, verbose)

    def encode_json_obj(self):
        return self._context_to_tag, self.backoff

    @classmethod
    def decode_json_obj(cls, obj):
        _context_to_tag, backoff = obj
        return cls(model=_context_to_tag, backoff=backoff)

    def context(self, tokens, index, history):
        #print(tokens[index], tokens[index-1])
        #print(len(history), index-1)
        tag_context = tuple(history[max(0, index-1):index])
        #print(tag_context, tokens[index], tokens[index-1])
        return tag_context, tokens[index]



brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.evaluate(test_sents))


t0 = nltk.DefaultTagger('NN')
t1 = minus1gramTagger(train_sents, backoff=t0)
#t2 = nltk.UnigramTagger(train_sents, backoff=t1)
t3 = nltk.BigramTagger(train_sents, backoff=t1)
print(t3.evaluate(test_sents))
