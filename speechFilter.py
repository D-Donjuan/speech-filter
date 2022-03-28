import string

class FileFilter:


    def __init__(self, textFile, stopWordsFile):
        self.textFile = textFile
        self.stopWordsFile = stopWordsFile

    def testReadTextFile(self):
        for i in self.textFile:
            print(i)

    def testReadStopWordsFile(self):
        for i in self.stopWordsFile:
            print(i)

    def removePunctuations(self):
        punctuations = string.punctuation

        for char in self.textFile:
            if char in punctuations:
                self.textFile = self.textFile.replace(char , "") 

    def removeStopWords(self):

        splitDebateText = self.textFile.split()
        splitStopWords = self.stopWordsFile.split()
        updatedDebateTextSplit = [word for word in splitDebateText if word.lower() not in splitStopWords]
        self.textFile = updatedDebateTextSplit






        
        
