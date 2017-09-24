# Information Retrieval
# Florida Atlantic University, Fall 2017
# Justin Johnson jjohn273
#
# Assignment 1: Using NLTK to conduct text preprocessing and cosine similarity calculation
# Given a collection of documents, conduct text preprocessing including tokenization, stop words removal, stemming, tf-idf calculation, and pairwise cosine similarity calculation using NLTK (similar to the lecture on 09/22 or you can choose other text processing tools you prefer). The following steps should be completed:
#
# Install Python 2 and NLTK (3 points)
# Tokenize the documents into words, remove stop words, and conduct stemming (5 points)
# Calculate tf-idf for each word in each document and generate document-word matrix (each element in the matrix is the tf-idf score for a word in a document) (7 points)
# Calculate pairwise cosine similarity for the documents (5 points)
# Please include your screen shots for each of the above steps and also the final results of the pairwise cosine similarity scores in your report.
import re
from nltk import word_tokenize
from os import listdir
from os.path import isfile, join, abspath
from modules.TokenizedDocument import TokenizedDocument  
  
print """
Assignment 1: NLTK text preprocessing and cosine similarity
Information Retrieval: Florida Atlantic University, Fall 2017
Justin J, jjohn273
"""

# get .txt files from data set directory
DATA_SET_DIR = abspath('hw1-dataset')
print '\nGetting List of text files from ' + DATA_SET_DIR
files = listdir(DATA_SET_DIR)
files = filter(lambda x: re.match(r'.*\.txt$', x, re.I), files)
print '\nFile list retrieved from ' + DATA_SET_DIR
for file in files:
  print file

print '\nTokenizing Each Document...'
tokenizedDocuments = []
for i, file in enumerate(files):
  tokenizedDocuments.append(TokenizedDocument(DATA_SET_DIR + '/' + file))
  tokenizedDocuments[i].tokenizeDocument()
  print 'Tokenized -> ' + tokenizedDocuments[i].toString()
  print 'isTokenized -> ' + str(tokenizedDocuments[i].isTokenized) + '\n'

