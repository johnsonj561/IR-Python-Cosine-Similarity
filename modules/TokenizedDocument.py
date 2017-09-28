# TokenizedDocument
# Accepts a file path as input
# Interface allows for text pre-processing and term list construction
# Term list is a dictionary s.t. key = term, value = term frequency tf
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


class TokenizedDocument:
	docID = 1
	def __init__(self, file_path):
		self.file_path = file_path
		self.docID = TokenizedDocument.docID
		self.isTokenized = False
		# termList[i] --> frequency of term i 
		self.termList = {}  
		TokenizedDocument.docID = TokenizedDocument.docID + 1

  # Tokenize the document
  # Apply stemming and remove stop words as defined in options
	def tokenizeDocument(self, stop_words=True, stemming=True): 
		doc = open(self.file_path, 'r')
		words = word_tokenize(doc.read())
		# apply stemming with PorterStemming algorithm
		if stemming == True:
			ps = PorterStemmer()
			words = map(lambda w: ps.stem(w), words)
		# remove stop words using nltk stop words
		if stop_words == True:
			nltk_stop_words = set(stopwords.words('english'))
			words = filter(lambda w: w not in nltk_stop_words, words)
		# count words and build document term list
		for word in words:
			if word in self.termList:
				self.termList[word] += 1
			else:
				self.termList[word] = 1
		self.isTokenized = True
  
	# 
	def removeStopWords(self, stop_words):
		self.termList = filter(lambda x: x in stop_words, self.termList)

	# Prints (term, term frequency) pair for every term in document
	def printTermList(self):
		for term, freq in self.termList.iteritems():
			print term + ', ' + str(freq)

	# Returns the term frequency tf for term
	def getTermFrequency(self, term):
		if term in self.termList:
			return self.termList[term]
		return 0

	def toString(self):
 		return 'Tokenized Document ID: ' + str(self.docID) + ',\Path = ' + self.file_path
