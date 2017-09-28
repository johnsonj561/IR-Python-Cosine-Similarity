# Information Retrieval
# Florida Atlantic University, Fall 2017
# Justin Johnson jjohn273

import re
import math
from nltk import word_tokenize
from os import listdir
from os.path import isfile, join, abspath
import numpy
from modules.TokenizedDocument import TokenizedDocument  
from modules.CosineSimilarity import get_cos_similarity_matrix

print """
Assignment 1: NLTK text preprocessing and cosine similarity
Information Retrieval: Florida Atlantic University, Fall 2017
Justin J, jjohn273
"""

# set the numpy print decision
numpy.set_printoptions(formatter={'float': '{: 0.5f}'.format})


# get .txt files from data set directory
DATA_SET_DIR = abspath('hw1-dataset')
print '\nGetting List of text files from ' + DATA_SET_DIR
files = listdir(DATA_SET_DIR)
files = filter(lambda x: re.match(r'.*\.txt$', x, re.I), files)
print '\nFile list retrieved from ' + DATA_SET_DIR


# tokenize each document individually
# apply pre-processing as defined in options
print '\nTokenizing Each Document...'
tokenized_documents = []
for file in files:
  doc = TokenizedDocument(DATA_SET_DIR + '/' + file)
  doc.tokenizeDocument()
  tokenized_documents.append(doc)
  print 'Tokenized -> ' + doc.toString()

  
# calculate document frequency df for every term
def buildTermDocFreqDict(tokenized_documents):
  df = {}
  for doc in tokenized_documents:
    for term in doc.termList:
      if term in df:
        df[term] += 1
      else:
        df[term] = 1
  return df

print '\nCalculating document frequency df for all terms'
term_df_dict = buildTermDocFreqDict(tokenized_documents)


# calculate inverse document frequency idf for every term
print '\nPrinting inverse document frequency idf  for every term'
term_idf_dict = {}
n = len(tokenized_documents)
for term, freq in term_df_dict.iteritems():
  term_idf_dict[term] = math.log10(n/(freq * 1.0))
  print term + ': ' + str(term_idf_dict[term])

	
# construct a term vs document matrix of tf-idf values
term_doc_tfidf_matrix = numpy.zeros((len(term_idf_dict), len(tokenized_documents)))
for i, term in enumerate(term_idf_dict):
  for j, doc in enumerate(tokenized_documents):
    tfidf = math.ceil((doc.getTermFrequency(term) * term_idf_dict[term])*10000) / 10000   # rounding to 4 decimal places
    term_doc_tfidf_matrix[i][j] = tfidf
		
		
# display tf-idf values
print '\nPrinting tf-idf for each term'
for idx, term in enumerate(term_idf_dict):
	print '{:<10}'.format(term) + str(term_doc_tfidf_matrix[idx])


# construct a dictionary of terms that point to lists of document tfidf values
term_doc_tfidf_dict = {}
for term, freq in term_idf_dict.iteritems():
  term_doc_tfidf_dict[term] = []
  for doc in tokenized_documents:
    tfidf = math.ceil((doc.getTermFrequency(term) * term_idf_dict[term])*10000) / 10000   # rounding to 4 decimal places
    term_doc_tfidf_dict[term].append(tfidf)
		

# Note - the tfidf matrix and dictionary are noth both needed, matrix alone is sufficient, dictionary is just alternative representation
  

# construct cosine similarity matrix whose values contain cosine similarity between every pair of documents
cos_similarity_matrix = numpy.zeros((len(tokenized_documents), len(tokenized_documents)))
for docRow, doc1 in enumerate(tokenized_documents):
  for docCol, doc2 in enumerate(tokenized_documents):
    cos_sim = get_cos_similarity_matrix(term_doc_tfidf_matrix[:, docRow], term_doc_tfidf_matrix[:, docCol])
    cos_similarity_matrix[docRow][docCol] = cos_sim


# printing cosine similarity matrix for all documents
print '\nPrinting cosine similarity matrix: '
print '\t Doc1     Doc2     Doc3     Doc4'
for idx, row in enumerate(cos_similarity_matrix):
	print 'Doc' + str(idx+1) + '\t' + str(row)