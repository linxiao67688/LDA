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
# read words from files
corpus_root = r"C:\Python27\nltk_data1"
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
# build the dictionary
dictionary = corpora.Dictionary(finitialwords)
# build the whole corpus words-frequency list
print  dictionary
corpus = [dictionary.doc2bow(document) for document in finitialwords]
print corpus
# calculate the tf-idf
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print str(corpus_tfidf)
# build the lda model
lda = gensim.models.ldamodel.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=10,update_every=0,passes=10)
index = similarities.MatrixSimilarity(lda[corpus])
lda.show_topics()
string = lda.show_topics(topn=10, formatted=False)
l = []
for w in string:
    l = l + w
    words = [item[1] for item in l]
    counts =[item[0] for item in l]
print words
print counts

lda.save("10topics.lda")
myfile = open("myfile.txt","w")
#myfile.write(string)
index.save("index10")
#model = models.ldamodel.LdaModel.load('20topics.pkl')
#print lda.print_topics(20)
#query
#query = estimate a background computer simple what why"
#query_bow = dictionary.doc2bow(query)
#query_lda = lda[query_bow]
#sims = index[query_lda]
#print query_lda























