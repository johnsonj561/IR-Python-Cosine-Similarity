# TokenizedDocument
# Accepts a file path as input
# Interface allows for text pre-processing and term list construction
# Term list is a dictionary s.t. key = term, value = term frequency tf
from nltk import word_tokenize

class TokenizedDocument:
  docID = 1
  def __init__(self, file_path):
    self.file_path = file_path
    self.docID = TokenizedDocument.docID
    self.isTokenized = False
    # termList[i] --> frequency of term i 
    self.termList = {}  
    TokenizedDocument.docID = TokenizedDocument.docID + 1

  def tokenizeDocument(self):
    doc = open(self.file_path, 'r')
    for word in word_tokenize(doc.read()):
      if word in self.termList:
        self.termList[word] += 1
      else:
        self.termList[word] = 1
    self.isTokenized = True
  
  def removeStopWords(self, stop_words):
    self.termList = filter(lambda x: x in stop_words, self.termList)
    
  def printTermList(self):
    for term, freq in self.termList.iteritems():
      print term + ', ' + str(freq)
    
  def toString(self):
   return 'Tokenized Document ID: ' + str(self.docID) + ',\Path = ' + self.file_path
  