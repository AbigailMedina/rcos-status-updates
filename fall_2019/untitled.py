class occurrance():
	def __init__(self, documentId, occurrances):
        self.documentId = documentId
        self.occurrances = occurrances#[indexOfOccurrance]
    def print(self):
    	for documentId in self.occurrances:
    		print(documentId, self.occurrances.get(documentId))#should print: documentid1 [occ1, occ2] for each document

class indexEntryInfo():
    def __init__(self, key, occurrances):
        self.key = key
        self.occurrances = occurrances #list of occurrance objects

    def print(self):
    	print("\nIndex entry: ", self.key,"\noccurrances:\n")

    	for occurrance in self.occurrances:
    		print(occurrance)
       

if __name__ == '__main__':

index = dict()
#adding word:
occ1 = occurrance("documentid1",[1, 50, 100])
occ2 = occurrance("documentid2",[0, 5, 10])

word = "apple"
occurances = [occ1,occ2]

wordInfo = indexEntryInfo(word,occurances)
index.add(word,wordInfo)

print(index)