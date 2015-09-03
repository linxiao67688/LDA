# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 10:21:49 2014

@author: Administrator
"""

from __future__ import division
from gensim import corpora, models, similarities
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import nltk, re, pprint
import pretreatment
def buildtopicmodel(filename,topicnum):
   pretreatment(filename)
#build the dictionary
   dictionary = corpora.Dictionary(finitialwords)
# build the whole corpus words-frequency list
   corpus = [dictionary.doc2bow(document) for document in finitialwords]
#print corpus
# calculate the tf-idf
   tfidf = models.TfidfModel(corpus)
   corpus_tfidf = tfidf[corpus]
# build the lda model
   lda = gensim.models.ldamodel.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=topicnum,update_every=0,passes=10)
   index = similarities.MatrixSimilarity(lda[corpus])
   lda.save(str(topicnum) + ".pkl")
#model = models.ldamodel.LdaModel.load('20topics.pkl')
   print lda.print_topics