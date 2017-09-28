## Information Retrieval
### Text Pre-Processing and Cosine Similarity with NLTK
----------------------
----------------------
### Application calculates the cosine similarity between the documents and outputs result as a matrix
### Steps:
#### Tokenize Text Documents
- read text files
- create word list for each document by splitting each document by word using NLTK's word_tokenize
- apply stemming to each word in word list, using NLTK's Porter Stemmer algorithm
- remove stop words from each document's word list
#### Calculate Document Frequency (df) for every term
- for each term, count total number of documents that contain term
#### Calculate Inverse Document Frequency (idf) for every term
- inverse document frequency will be used in tf-idf metric, lowering term values that are less rare (appear in more docs)
- idf = log(N/df)
#### Calculate tf-idf for every term of every document
- tf-idf matrix is constructed which contains the tf-idf metric for every term of every document
#### Vector representation of documents
- each document is now represented as a vector whose elements consist of tf-idf values
#### Calculate cosine similarity for every pair of documents
- The cosine similarity is calculated for every pair of documents
- result is a cosine similarity matrix where higher values in cosine similarity correspond to a higher correlation

