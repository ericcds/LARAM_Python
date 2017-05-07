__author__ = 'zhangyin, ecarr'

import numpy as np
import os
import nltk
from nltk.stem.porter import *
from nltk import FreqDist
import math
from Structure import *

stemmer = PorterStemmer()



##### run code #######

# import numpy as np
# (corpus,Vocab,Count,VocabDict)=np.load("./output/yelp_mp1_corpus.npy")

analyzer = Bootstrapping()
loadfilepath = "data/init_aspect_word.txt"
load_Aspect_Terms(analyzer,loadfilepath,VocabDict)

(corpus,Vocab,Count,VocabDict)=np.load("output/yelp_sanitation_corpus.npy")
data = Corpus(corpus, Vocab, Count,VocabDict)
# 15 mins



Add_Aspect_Keywords(analyzer, 5, 5, data)

savefilepath = 'temp_aspect_words_yelp_sanitation.txt'
save_Aspect_Keywords_to_file(analyzer,savefilepath,Vocab)

create_all_W(analyzer,data)
outputfolderpath = "data/output_data_for_rating/"
produce_data_for_rating(analyzer,data,outputfolderpath)
