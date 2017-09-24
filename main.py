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
import math
from nltk import word_tokenize
from os import listdir
from os.path import isfile, join, abspath
from modules.TokenizedDocument import TokenizedDocument  
from modules.CosineSimilarity import get_cos_similarity_matrix
import numpy

print """
Assignment 1: NLTK text preprocessing and cosine similarity
Information Retrieval: Florida Atlantic University, Fall 2017
Justin J, jjohn273
"""


def buildTermDocFreqDict(tokenized_documents):
  df = {}
  for doc in tokenized_documents:
    for term in doc.termList:
      if term in df:
        df[term] += 1
      else:
        df[term] = 1
  return df


# get .txt files from data set directory
DATA_SET_DIR = abspath('hw1-dataset-test')
print '\nGetting List of text files from ' + DATA_SET_DIR
files = listdir(DATA_SET_DIR)
files = filter(lambda x: re.match(r'.*\.txt$', x, re.I), files)
print '\nFile list retrieved from ' + DATA_SET_DIR


# tokenize each document individually
# TODO - Apply stemming and stop words
# TODO********************************
print '\nTokenizing Each Document...'
tokenized_documents = []
for file in files:
  doc = TokenizedDocument(DATA_SET_DIR + '/' + file)
  doc.tokenizeDocument()
  tokenized_documents.append(doc)
  print 'Tokenized -> ' + doc.toString()
  print 'isTokenized -> ' + str(doc.isTokenized) + '\n'
  
  
# calculate document frequency df for every term
term_df_dict = buildTermDocFreqDict(tokenized_documents)


# calculate inverse document frequency idf for every term
term_idf_dict = {}
n = len(tokenized_documents)
for term, freq in term_df_dict.iteritems():
  term_idf_dict[term] = math.log10(n/(freq * 1.0))
  
  
# construct a term vs document matrix of tf-idf values
term_doc_tfidf_matrix = numpy.zeros((len(term_idf_dict), len(tokenized_documents)))
for i, term in enumerate(term_idf_dict):
  for j, doc in enumerate(tokenized_documents):
    tfidf = math.ceil((doc.getTermFrequency(term) * term_idf_dict[term])*10000) / 10000   # rounding to 4 decimal places
    term_doc_tfidf_matrix[i][j] = tfidf
    
    
# construct a dictionary of terms that point to lists of document tfidf values
term_doc_tfidf_dict = {}
for term, freq in term_idf_dict.iteritems():
  print 'Term: ' + term
  term_doc_tfidf_dict[term] = []
  for doc in tokenized_documents:
    tfidf = math.ceil((doc.getTermFrequency(term) * term_idf_dict[term])*10000) / 10000   # rounding to 4 decimal places
    term_doc_tfidf_dict[term].append(tfidf)
    print '\tDocument ' + str(doc.docID) + ', ' + str(tfidf)
    

# Note - the tfidf matrix and dictionary are noth both needed, matrix alone is sufficient, dictionary is just another representation
  
print '\ntfidf matrix: ' 
print term_doc_tfidf_matrix


# construct cosine similarity matrix whose values contain cosine similarity between every pair of documents
cos_similarity_matrix = numpy.zeros((len(tokenized_documents), len(tokenized_documents)))
for docRow, doc1 in enumerate(tokenized_documents):
  #for each document column
  for docCol, doc2 in enumerate(tokenized_documents):
    cos_sim = get_cos_similarity_matrix(term_doc_tfidf_matrix[:, docRow], term_doc_tfidf_matrix[:, docCol])
#    print 'row ' + str(docRow) + ', col ' + str(docCol) + ' -> ' + str(cos_sim)
    cos_similarity_matrix[docRow][docCol] = cos_sim


print '\nJustins Cosine Similarity Function'
print cos_similarity_matrix



#
#sklearn_cos_similarity_matrix = numpy.zeros((len(tokenized_documents), len(tokenized_documents)))
#for docRow, doc1 in enumerate(tokenized_documents):
#  for docCol, doc2 in enumerate(tokenized_documents):
#    sklearn_cos_similarity_matrix[docRow][docCol] = cosine_similarity(term_doc_tfidf_matrix[docRow], term_doc_tfidf_matrix[docCol])
#print '\nsklearns Cosine Similarity Function'
#print sklearn_cos_similarity_matrix
#  
#
#    
#

    




