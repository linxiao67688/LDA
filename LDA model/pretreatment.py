from __future__ import division
from gensim import corpora, models, similarities
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import nltk, re, pprint
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import BracketParseCorpusReader
from nltk.corpus import brown
from nltk.corpus import nps_chat
import enchant
from nltk.corpus import stopwords
d = enchant.Dict("en_US")
def LDA_pretreatment(filename):
# read words from files
     corpus_root = filename
     file_pattern = r".*"
     ptb = PlaintextCorpusReader(corpus_root,file_pattern)
# remove the words whose lenth>6
     initialwords = [[w for w in ptb.words(fileid) if len(w)>6]for fileid in ptb.fileids()]
# remove the words that were spelled wrong
     spellcheckedwords = [[w for w in document if d.check(w)]for document in initialwords]
# translate to low litter
     lowerwords =[[w.lower() for w in document]for document in spellcheckedwords]
# 
     wnl = nltk.WordNetLemmatizer()
     rectifywords = [[wnl.lemmatize(s) for s in document]for document in lowerwords]
# remove the stopwords
     stopwords = nltk.corpus.stopwords.words('english')
     finitialwords = [[w for w in document if w not in stopwords]for document in rectifywords]
     return finitialwords