from Tkinter import*
from nltk.corpus import brown
from nltk.corpus import nps_chat
from gensim import corpora, models,similarities
import enchant
from nltk.corpus import stopwords
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import nltk, re, pprint
from nltk.corpus import brown
from pretreatment import LDA_pretreatment
import corpuslda
#from wordcloud0 import make_wordcloud
import numpy as np
from PIL import Image
font_path = "simsun.ttc"
root = Tk()
root.title("Scientific Articles Recommendation System")
Label(root,text="please choose the scientific article from the listbox.",compound="left",bitmap = 'gray25').grid(column=1,columnspan=5,row=0,rowspan=1)
Label(root,text="you can see the first three topics in the follow textbox.",compound="left",bitmap = 'gray25').grid(column=10,columnspan=5,row=0,rowspan=1)
Label(root,text="you can see the title of the relative articles in the follow textbox",compound="left",bitmap = 'gray25').grid(column=10,columnspan=5,row=11,rowspan=1)
#t = Text().grid(column=10,columnspan=5,row=3,rowspan=40)
#t1 = Text().grid(column=10,columnspan=5,row=12,rowspan=40)
sen = ""
def readfile(list):
    content = ""
    for item in list:
        sen = ""
        r = r"C:\Python27\nltk_data\1"
        f = open(r  +" "+ "(" + str(item) +").txt")
        sen = str(item) + "articles: "
        i = 3
        while i>0:
            s = f.readline()
            i = i-1
            sen = sen + s + "\n"
        content = content + sen + "\n"
    return content
def printList(event):
    print 
lb = Listbox(root)
lb.bind('<Double-Button-1>',printList)
for item in ['article1','article2','article3']:
   lb.insert(END,item)
lb.grid(column=1,columnspan=5,row=1,rowspan=20)
#text = Text().grid(column=10,columnspan=5,row=3,rowspan=40)
text = Text(root,width = 100,height = 10)
text.grid(column=10,columnspan=5,row=1,rowspan=10)
text1 = Text(root,width = 100,height = 30)
text1.grid(column=10,columnspan=5,row=12,rowspan=20)
na = r"C:\Python27\nltk_data1"  
dictionary = corpora.Dictionary(LDA_pretreatment(na))
corpus = [dictionary.doc2bow(document) for document in LDA_pretreatment(na)]
def botton1():
    text.delete(0.0,END)
    text1.delete(0.0,END)
    model = models.ldamodel.LdaModel.load('50topics.pkl')
    simindex = load("index50")
    corpusf = corpus[0]
    query_lda = model[corpusf]
    text.insert(1.0,"the first ten topoics are:")
    text.insert(2.0,"\n")
    text.insert(3.0,str(model.show_topics(topn=3, formatted=True)))
    string = model.show_topics(topn=10, formatted=False)
    print string
    l = []
    for w in string:
        l = l + w
    words = [item[1] for item in l]
    counts =[item[0] for item in l]
    print words
    print counts
    sims = simindex[query_lda]
    print sims
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1],reverse=False)
    sort_sim =[item[0] for item in sort_sims[0:10]]
    print sort_sim
    text.insert(50.0,"\n")
    text.insert(52.0,"the first ten relative articles are:")
    text.insert(53.0,"\n")
    text.insert(54.0,str(sort_sims[0:10]))
    text1.insert(1.0,str(readfile(sort_sim)))
    #im=Image.open("1.png")
    #im.show()
def botton2():
    text.delete(0.0,END)
    text1.delete(0.0,END)
    model = models.ldamodel.LdaModel.load('100topics.pkl')
    simindex = load("index100")
    corpusf = corpus[0]
    query_lda = model[corpusf]
    text.insert(1.0,"the first ten topoics are:")
    text.insert(2.0,"\n")
    text.insert(3.0,str(model.show_topics(topn=3)))
    string = model.show_topics(topn=10, formatted=False)
    l = []
    for w in string:
        l = l + w
    words = [item[1] for item in l]
    counts =[item[0] for item in l]
    print words
    print counts
    sims = simindex[query_lda]
    #print sims
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1],reverse=False)
    sort_sim =[item[0] for item in sort_sims[0:10]]
    text.insert(50.0,"\n")
    text.insert(52.0,"the first ten relative articles are:")
    text.insert(53.0,"\n")
    text.insert(54.0,str(sort_sims[0:10]))
    text1.insert(1.0,str(readfile(sort_sim)))
def botton3():
    text.delete(0.0,END)
    text1.delete(0.0,END)
    model = models.ldamodel.LdaModel.load('200topics.pkl')
    simindex = load("index200")
    corpusf = corpus[0]
    query_lda = model[corpusf]
    text.insert(1.0,"the first ten topoics are:")
    text.insert(2.0,"\n")
    text.insert(3.0,str(model.show_topics(topn=3)))
    string = model.show_topics(topn=10, formatted=False)
    l = []
    for w in string:
        l = l + w
    words = [item[1] for item in l]
    counts =[item[0] for item in l]
    print words
    print counts
    #make_wordcloud(words, counts, font_path)
    myfile = open("myfile2.txt","w")
   # myfile.write(string)
    sims = simindex[query_lda]
    print sims
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1],reverse=False)
    sort_sim =[item[0] for item in sort_sims[0:10]]
    text.insert(52.0,"the first ten relative articles are:")
    text.insert(54.0,"\n")
    text.insert(55.0,str(sort_sims[0:10]))
    text1.insert(1.0,str(readfile(sort_sim)))
button1=Button(root,text=" search the relative articles with 50topics ",command=botton1,compound="left",bitmap = 'gray12')
button2=Button(root,text="search the relative articles with 100topics",command=botton2,compound="left",bitmap = 'gray12')
button3=Button(root,text="search the relative articles with 200topics",command=botton3,compound="left",bitmap = 'gray12')
button1.grid(column=1,columnspan=5,row=21,rowspan=1)
button2.grid(column=1,columnspan=5,row=22,rowspan=1)
button3.grid(column=1,columnspan=5,row=23,rowspan=1)

#scrollbar.configure(command=listbox.yview
root.mainloop()