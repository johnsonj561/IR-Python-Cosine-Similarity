# Information Retrieval
# Florida Atlantic University, Fall 2017
# Justin Johnson jjohn273
#
# Assignment 1: Using NLTK to conduct text preprocessing and cosine similarity calculation
# Given a collection of documents, conduct text preprocessing including tokenization, stop words removal, stemming, tf-idf calculation, and pairwise cosine similarity calculation using NLTK (similar to the lecture on 09/22 or you can choose other text processing tools you prefer). The following steps should be completed:
# Install Python 2 and NLTK (3 points)
# Tokenize the documents into words, remove stop words, and conduct stemming (5 points)
# Calculate tf-idf for each word in each document and generate document-word matrix (each element in the matrix is the tf-idf score for a word in a document) (7 points)
# Calculate pairwise cosine similarity for the documents (5 points)
# Please include your screen shots for each of the above steps and also the final results of the pairwise cosine similarity scores in your report.
import re
from os import listdir
from os.path import join, abspath
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print """
Assignment 1: NLTK text preprocessing and cosine similarity
Information Retrieval: Florida Atlantic University, Fall 2017
Justin J, jjohn273
"""

# get .txt files from data set directory
data_dir = 'hw1-dataset'
DATA_SET_DIR = abspath(data_dir)
print '\nGetting List of text files from ' + DATA_SET_DIR
files = listdir(DATA_SET_DIR)
files = filter(lambda x: re.match(r'.*\.txt$', x, re.I), files)
print '\nFile list retrieved from ' + DATA_SET_DIR


# define stemming mechanism and stop words
ps = PorterStemmer()
nltk_stop_words = set(stopwords.words('english'))


# build corpus: list of documents
# stop words are ignored, words are stemmed using PorterStemmer
corpus = []
for f in files:
	strm = open(DATA_SET_DIR + '/' + f, 'r')
	# using nltk word tokenizer to split file into word list
	words = word_tokenize(strm.read())
	# using filter to remove stop words from word list
	words = filter(lambda w: w not in nltk_stop_words, words)
	# using map to stem words in word list
	words = map(lambda w: ps.stem(str(w)), words)
	# joining words into string and adding to corpus list
	corpus.append(' '.join(words))

	
# Using sklearn's tfidfvectorizer to construct tfidf matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
terms = vectorizer.get_feature_names()
print '\nPrinting tfidf values for each term:' 
print '\t\t Doc1         Doc2        Doc3        Doc4'
for idx, row in enumerate(tfidf_matrix.toarray().transpose()):
	print '{:<10}'.format(terms[idx]) + '\t' + str(row)

	
# Using sklearn's cosine_similarty to calculate cosine similarity between all documents
cos_sim_matrix = cosine_similarity(tfidf_matrix)
print '\nPrinting cosine similarity matrix: '
print '\t Doc1         Doc2        Doc3        Doc4        Doc5'
for idx, row in enumerate(cos_sim_matrix):
	print 'Doc' + str(idx+1) + '\t' + str(row)


print '\nComplete.'